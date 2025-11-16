import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="Netflix User Behavior Analytics", layout="wide", page_icon=":clapper:", initial_sidebar_state="expanded")
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

movies = pd.read_csv('data/raw/movies.csv')
reviews = pd.read_csv('data/raw/reviews.csv')
users = pd.read_csv('data/raw/users.csv')

st.sidebar.header("Choose your filters:")
# Create for Country
country = st.sidebar.multiselect("Pick your Country", movies["country_of_origin"].unique())

# Create for Genre
genre = st.sidebar.multiselect("Pick your Genre", movies["genre_primary"].unique())

movies_filtered = movies.copy()

# Filter by country
if country:
    movies_filtered = movies_filtered[movies_filtered["country_of_origin"].isin(country)]

# Filter by genre
if genre:
    movies_filtered = movies_filtered[movies_filtered["genre_primary"].isin(genre)]

with col1:
    st.subheader("Movies by Genre")

    genre_count = movies_filtered['genre_primary'].value_counts()

    fig_genre = px.bar(
        x=genre_count.values,
        y=genre_count.index,
        labels={'x': 'Number of Movies', 'y': 'Genre'}
    )

    st.plotly_chart(fig_genre, use_container_width=True)

with col2:
    st.subheader("Movies by Country of Origin")

    country_count = movies_filtered['country_of_origin'].value_counts()

    fig_country = px.pie(
        names=country_count.index,
        values=country_count.values
    )

    st.plotly_chart(fig_country, use_container_width=True)





