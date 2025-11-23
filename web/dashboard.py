# app.py
import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

st.set_page_config(layout="wide", page_title="Netflix Analytics Dashboard")
st.title(" :bar_chart: Netflix User Behavior Analytics Dashboard")
st.markdown("""
    <style>
    div.block-container {
        padding-top: 2.5rem;
    }
    h1 {
        font-size: 32px !important;
    }
    h2 {
        font-size: 16px !important;
    }
    </style>
""", unsafe_allow_html=True)
def load_data(movies_path="data/raw/movies.csv", reviews_path="data/raw/reviews.csv"):
    # Load CSVs (paths provided in this session)
    movies = pd.read_csv(movies_path)
    reviews = pd.read_csv(reviews_path)

    # Parse dates (robust parsing)
    for col in ["review_date", "date", "created_at"]:
        if col in reviews.columns:
            reviews["review_date"] = pd.to_datetime(reviews[col], errors="coerce")
            break
    if "review_date" not in reviews.columns:
        # fallback: try to parse any column that looks like a date
        for c in reviews.columns:
            try:
                tmp = pd.to_datetime(reviews[c], errors="coerce")
                if tmp.notna().sum() > 0:
                    reviews["review_date"] = tmp
                    break
            except Exception:
                pass

    # Movies: there is a release_year column in your CSVs based on inspection
    if "release_year" in movies.columns:
        movies["release_year"] = pd.to_numeric(movies["release_year"], errors="coerce")
    # If there is a release_date-like column, try parse to datetime (robust)
    for c in ["release_date", "date_added", "released", "premiere_date"]:
        if c in movies.columns:
            movies["release_date"] = pd.to_datetime(movies[c], errors="coerce")
            break

    return movies, reviews

movies, reviews = load_data()

# --- JOIN (merge) use-case: combine movie metadata with reviews
# The app intentionally uses pandas.merge here (per your instructions).
# We merge reviews -> movies on 'movie_id'. This allows analyses like avg rating per genre.
merged = pd.merge(reviews, movies, on="movie_id", how="left")

# Sidebar filters
st.sidebar.header("Filters")
content_types = ["All"] + sorted(movies["content_type"].dropna().unique().tolist())
content_choice = st.sidebar.selectbox("Content type", content_types)

countries = ["All"] + sorted(movies["country_of_origin"].dropna().unique().tolist())
country_choice = st.sidebar.selectbox("Country of origin", countries)

# Date filter for reviews (default full range)
if "review_date" in reviews.columns:
    min_date = reviews["review_date"].min()
    max_date = reviews["review_date"].max()
    if pd.isna(min_date):
        min_date = datetime(2000,1,1)
    if pd.isna(max_date):
        max_date = datetime.now()
    date_range = st.sidebar.date_input("Review date range", [min_date.date(), max_date.date()])
else:
    date_range = None

# Apply filters to merged df
df = merged.copy()
if content_choice != "All":
    df = df[df["content_type"] == content_choice]
if country_choice != "All":
    df = df[df["country_of_origin"] == country_choice]
if date_range and len(date_range) == 2 and "review_date" in df.columns:
    start, end = pd.to_datetime(date_range[0]), pd.to_datetime(date_range[1])
    df = df[(df["review_date"] >= start) & (df["review_date"] <= end)]

# Overview metrics (like monthly spending summary in a banking app)
cols = st.columns(4)
total_titles = movies.shape[0]
total_reviews = reviews.shape[0]
# attempt to compute average rating using common rating column name 'rating'
avg_rating = None
if "rating" in reviews.columns:
    avg_rating = reviews["rating"].dropna().astype(float).mean()
elif "sentiment_score" in reviews.columns:
    avg_rating = reviews["sentiment_score"].dropna().astype(float).mean()

cols[0].metric("Total titles (movies/series)", f"{total_titles:,}")
cols[1].metric("Total reviews", f"{total_reviews:,}")
cols[2].metric("Avg rating / sentiment", f"{avg_rating:.2f}" if avg_rating is not None else "—")
# Example "monthly equivalent" metric: reviews in selected date range
if "review_date" in reviews.columns and date_range:
    reviews_in_range = reviews[(reviews["review_date"] >= pd.to_datetime(date_range[0])) & (reviews["review_date"] <= pd.to_datetime(date_range[1]))].shape[0]
    cols[3].metric("Reviews in selection", f"{reviews_in_range:,}")
else:
    cols[3].metric("Reviews in selection", "—")

st.markdown("---")

# --- Category breakdown (genre) like category spend breakdown
st.header("Genre / Category Breakdown")
# Combine primary and secondary genre columns if present
genre_cols = []
if "genre_primary" in movies.columns:
    genre_cols.append("genre_primary")
if "genre_secondary" in movies.columns:
    genre_cols.append("genre_secondary")
if not genre_cols:
    # fallbacks
    for c in ["genres", "genre", "category"]:
        if c in movies.columns:
            genre_cols.append(c)
            break

# Build genre counts using movies dataframe (not merged), split if needed
genre_counts = {}
if genre_cols:
    for _, row in movies.iterrows():
        vals = []
        for c in genre_cols:
            if pd.notna(row.get(c, None)):
                # support comma-separated lists in a single column
                vals += [v.strip() for v in str(row[c]).split(",") if v.strip()]
        for g in vals:
            genre_counts[g] = genre_counts.get(g, 0) + 1

genre_df = pd.DataFrame([{"genre": g, "count": cnt} for g, cnt in genre_counts.items()])
if genre_df.shape[0] == 0:
    st.info("No genre information found in movies file.")
else:
    genre_df = genre_df.sort_values("count", ascending=False)
    fig_pie = px.pie(genre_df.head(10), names="genre", values="count", title="Top genres (by title count)")
    fig_bar = px.bar(genre_df.head(15), x="genre", y="count", title="Top genres (bar)")
    c1, c2 = st.columns((1,1))
    c1.plotly_chart(fig_pie, use_container_width=True)
    c2.plotly_chart(fig_bar, use_container_width=True)

st.markdown("---")

# --- Trends (monthly reviews, releases)
st.header("Trends Over Time")

# Reviews per month (from reviews)
if "review_date" in df.columns:
    rev_ts = df.copy()
    rev_ts["month"] = rev_ts["review_date"].dt.to_period("M").astype(str)
    rev_trend = rev_ts.groupby("month").agg(
        reviews_count=("review_id", "count"),
        avg_sentiment=("sentiment_score", "mean") if "sentiment_score" in rev_ts.columns else ("rating", "mean")
    ).reset_index().sort_values("month")
    # Plot reviews count
    fig_rev_count = px.line(rev_trend, x="month", y="reviews_count", title="Reviews per month (selection)")
    fig_rev_sent = None
    if "avg_sentiment" in rev_trend.columns:
        fig_rev_sent = px.line(rev_trend, x="month", y="avg_sentiment", title="Avg sentiment / rating per month")
    c1, c2 = st.columns(2)
    c1.plotly_chart(fig_rev_count, use_container_width=True)
    if fig_rev_sent:
        c2.plotly_chart(fig_rev_sent, use_container_width=True)
else:
    st.info("No review date column parsed — unable to show review trends.")

# Releases per year-month (from movies release_date or release_year)
if "release_date" in movies.columns and movies["release_date"].notna().any():
    m = movies.copy()
    m["month"] = m["release_date"].dt.to_period("M").astype(str)
    releases = m.groupby("month").size().reset_index(name="releases").sort_values("month")
    fig_releases = px.bar(releases, x="month", y="releases", title="Titles added by month")
    st.plotly_chart(fig_releases, use_container_width=True)
elif "release_year" in movies.columns:
    counts = movies.groupby("release_year").size().reset_index(name="titles")
    counts = counts[counts["release_year"].notna()].sort_values("release_year")
    fig_release_year = px.bar(counts, x="release_year", y="titles", title="Titles by release year")
    st.plotly_chart(fig_release_year, use_container_width=True)
else:
    st.info("No release date or release_year data present to show release trends.")

st.markdown("---")

# --- Top lists / comparisons (like top spending categories)
st.header("Top Titles & Genre-level Metrics")

# Top movies by average review rating (use merged dataframe)
if "imdb_rating" in df.columns:
    top_movies = df.groupby(["movie_id", "title"], dropna=False).agg(
        avg_rating=("imdb_rating", "mean"),
        review_count=("review_id", "count"),
        avg_sentiment=("sentiment_score", "mean")
    ).reset_index().sort_values(["avg_rating", "review_count"], ascending=[False, False]).head(20)
    st.subheader("Top movies by avg rating (from reviews)")
    st.dataframe(top_movies[["movie_id", "title", "avg_rating", "review_count", "avg_sentiment"]].round(3))
else:
    st.info("No numeric rating column found in reviews.")

# Genre-level rating (requires merged + genre info)
if genre_df.shape[0] > 0 and "rating" in df.columns:
    # Explode genres from merged df: look at primary and secondary
    def extract_genres(row):
        gs = []
        for c in ["genre_primary", "genre_secondary", "genres", "genre", "category"]:
            if c in row and pd.notna(row[c]):
                # support comma/pipe/semicolon separation
                gs += [g.strip() for g in str(row[c]).replace("|", ",").replace(";", ",").split(",") if g.strip()]
        return gs

    tmp = df.copy()
    tmp["genres_list"] = tmp.apply(extract_genres, axis=1)
    tmp = tmp.explode("genres_list")
    tmp = tmp[tmp["genres_list"].notna()]

    genre_rating = tmp.groupby("genres_list").agg(
        avg_rating=("rating", "mean"),
        reviews_count=("review_id", "count")
    ).reset_index().rename(columns={"genres_list": "genre"}).sort_values("avg_rating", ascending=False)
    if not genre_rating.empty:
        fig = px.bar(genre_rating.head(15), x="genre", y="avg_rating", title="Average rating by genre (top 15)")
        st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# --- Data explorer + download
st.header("Data Explorer & Download")
st.write("Preview of merged dataset (reviews joined to movies via `movie_id`):")
st.dataframe(df.head(100))

# allow download of current filtered merged view
@st.cache_data
def to_csv_bytes(df_in: pd.DataFrame):
    return df_in.to_csv(index=False).encode("utf-8")

st.download_button("Download filtered merged data (CSV)", to_csv_bytes(df), file_name="merged_reviews_movies.csv")


