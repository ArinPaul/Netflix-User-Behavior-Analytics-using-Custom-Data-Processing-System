import my_pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Netflix Analytics Dashboard", layout="wide", page_icon=":clapper:", initial_sidebar_state="expanded")
st.title(" :bar_chart: Netflix User Behavior Analytics Dashboard")
st.markdown("""
    <style>
    div.block-container {
        padding-top: 2.5rem;
    }
    h1 {
        font-size: 28px !important;
    }
    h2 {
        font-size: 16px !important;
    }
    </style>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

movies = pd.read_csv('data/movies.csv')
reviews = pd.read_csv('data/reviews.csv')

st.sidebar.header("Choose your filters:")

country = st.sidebar.multiselect("Pick your Country", movies["country_of_origin"].unique("country_of_origin"))

genre = st.sidebar.multiselect("Pick your Genre", movies["genre_primary"].unique("genre_primary"))

movies_filtered = movies.copy()
if country:
    mask = movies_filtered.isin("country_of_origin", country)
    movies_filtered = movies_filtered[mask]

if genre:
    mask = movies_filtered.isin("genre_primary", genre)
    movies_filtered = movies_filtered[mask]

with col1:
    st.subheader("Movies by Genre")

    genre_count = movies_filtered.groupby('genre_primary').agg({'genre_primary': 'count'})
    fig_genre = px.bar(
        x=genre_count['genre_primary'].data['genre_primary'],
        y=genre_count['genre_primary_count'].data['genre_primary_count'],
        labels={'x': 'Number of Movies', 'y': 'Genre'}
    )

    st.plotly_chart(fig_genre, use_container_width=True)

with col2:
    st.subheader("Movies by Country of Origin")

    country_count = movies_filtered.groupby('country_of_origin').agg({'country_of_origin': 'count'})

    fig_country = px.pie(
        names=country_count['country_of_origin'].data['country_of_origin'],
        values=country_count['country_of_origin_count'].data['country_of_origin_count'],
    )

    st.plotly_chart(fig_country, use_container_width=True)

col3, col4 = st.columns(2)
with col3:
    st.subheader("Top 10 Movies by Average Rating")

    merged = movies_filtered.merge(reviews, left_on='movie_id', right_on='movie_id')

    avg_ratings = merged.groupby('title').agg({'rating': 'avg'})

    top_10_movies = avg_ratings.sort_values(by='rating_avg', ascending=False).head(10)

    st.table(
    top_10_movies[['title', 'rating_avg']].rename(
        columns={
            'title': 'Movie Title',
            'rating_avg': 'Average Rating'
        }
    ).data)

with col4:
    st.subheader("Ratings Distribution")

    fig_ratings_dist = px.histogram(
        merged.data,
        x='rating',
        nbins=20,
        labels={'rating': 'Rating'},
        title='Distribution of Movie Ratings'
    )

    st.plotly_chart(fig_ratings_dist, use_container_width=True)