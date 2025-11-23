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
    movies_filtered = movies_filtered[movies_filtered["country_of_origin"].isin(country)]

if genre:
    movies_filtered = movies_filtered[movies_filtered["genre_primary"].isin(genre)]

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

