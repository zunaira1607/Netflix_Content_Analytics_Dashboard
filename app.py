import streamlit as st
import pandas as pd
import plotly.express as px
PRIMARY_COLOR = "#E50914"
BACKGROUND = "#141414"
CARD_COLOR = "#222222"
TEXT_COLOR = "#FFFFFF"
st.markdown(f"""
<style>
.stApp {{
    background-color: {BACKGROUND};
    color: {TEXT_COLOR};
}}

[data-testid="stMetric"] {{
    background-color: {CARD_COLOR};
    padding: 15px;
    border-radius: 10px;
}}

h1, h2, h3 {{
    color: {PRIMARY_COLOR};
}}
</style>
""", unsafe_allow_html=True)

# ---------------------------
# PAGE CONFIG
# ---------------------------

st.set_page_config(
    page_title="Netflix Dashboard",
    page_icon="🎬",
    layout="wide"
)

# ---------------------------
# LOAD DATA
# ---------------------------

df = pd.read_csv("C:/Users/User/OneDrive/Desktop/NCA/data/netflix_cleaned.csv")

# ---------------------------
# SIDEBAR
# ---------------------------

st.sidebar.title("🎯 Filters")

type_filter = st.sidebar.multiselect(
    "Select Type",
    options=df["type"].unique(),
    default=df["type"].unique()
)

rating_filter = st.sidebar.multiselect(
    "Select Rating",
    options=df["rating"].unique(),
    default=df["rating"].unique()
)

year_filter = st.sidebar.slider(
    "Release Year",
    int(df["release_year"].min()),
    int(df["release_year"].max()),
    (
        int(df["release_year"].min()),
        int(df["release_year"].max())
    )
)

# ---------------------------
# FILTER DATA
# ---------------------------

filtered_df = df[
    (df["type"].isin(type_filter))
    &
    (df["rating"].isin(rating_filter))
    &
    (df["release_year"].between(year_filter[0], year_filter[1]))
]

# ---------------------------
# TITLE
# ---------------------------

st.title("🎬 Netflix Content Analytics Dashboard")
st.markdown("---")

# ---------------------------
# KPI CARDS
# ---------------------------

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Titles",
    len(filtered_df)
)

col2.metric(
    "Movies",
    len(filtered_df[filtered_df["type"] == "Movie"])
)

col3.metric(
    "TV Shows",
    len(filtered_df[filtered_df["type"] == "TV Show"])
)

col4.metric(
    "Ratings",
    filtered_df["rating"].nunique()
)

st.markdown("---")

# ---------------------------
# PIE CHART
# ---------------------------

col1, col2 = st.columns(2)

with col1:

    fig = px.pie(
        filtered_df,
        names="type",
        title="Movies vs TV Shows",
        hole=0.4,
        color_discrete_sequence=px.colors.qualitative.Bold
    )

    st.plotly_chart(fig, use_container_width=True)

# ---------------------------
# RATINGS
# ---------------------------

with col2:

    ratings = (
        filtered_df["rating"]
        .value_counts()
        .reset_index()
    )

    ratings.columns = ["Rating", "Count"]

    fig = px.bar(
        ratings,
        x="Count",
        y="Rating",
        orientation="h",
        title="Ratings Distribution",
        color="Count",
        color_continuous_scale="reds"
    )

    st.plotly_chart(fig, use_container_width=True)

# ---------------------------
# TOP COUNTRIES
# ---------------------------

countries = filtered_df.assign(
    country=filtered_df["country"].str.split(", ")
).explode("country")

country_counts = (
    countries["country"]
    .value_counts()
    .head(10)
    .reset_index()
)

country_counts.columns = ["Country", "Count"]

# ---------------------------
# TOP GENRES
# ---------------------------

genres = filtered_df.assign(
    genre=filtered_df["listed_in"].str.split(", ")
).explode("genre")

genre_counts = (
    genres["genre"]
    .value_counts()
    .head(10)
    .reset_index()
)

genre_counts.columns = ["Genre", "Count"]

col1, col2 = st.columns(2)

with col1:

    fig = px.bar(
        country_counts,
        x="Count",
        y="Country",
        orientation="h",
        title="Top 10 Countries",
        color="Count",
        color_continuous_scale="viridis"
    )

    st.plotly_chart(fig, use_container_width=True)

with col2:

    fig = px.bar(
        genre_counts,
        x="Genre",
        y="Count",
        title="Top Genres",
        color="Count",
        color_continuous_scale="plasma"
    )

    st.plotly_chart(fig, use_container_width=True)

# ---------------------------
# CONTENT ADDED OVER YEARS
# ---------------------------

if "added_year" in filtered_df.columns:

    yearly = (
        filtered_df["added_year"]
        .value_counts()
        .sort_index()
        .reset_index()
    )

    yearly.columns = ["Year", "Count"]

    fig = px.line(
        yearly,
        x="Year",
        y="Count",
        markers=True,
        title="Content Added by Year"
    )

    st.plotly_chart(fig, use_container_width=True)

# ---------------------------
# MOVIE DURATION
# ---------------------------

movies = filtered_df[
    filtered_df["type"] == "Movie"
].copy()

movies["duration_min"] = (
    movies["duration"]
    .str.extract(r"(\d+)")
)

movies["duration_min"] = pd.to_numeric(
    movies["duration_min"],
    errors="coerce"
)

fig = px.histogram(
    movies,
    x="duration_min",
    nbins=20,
    title="Movie Duration Distribution"
)

st.plotly_chart(fig, use_container_width=True)

# ---------------------------
# DATA TABLE
# ---------------------------

st.subheader("Netflix Dataset")

st.dataframe(filtered_df)

# ---------------------------
# DOWNLOAD BUTTON
# ---------------------------

st.download_button(
    "⬇ Download Filtered Data",
    filtered_df.to_csv(index=False),
    file_name="filtered_netflix_data.csv",
    mime="text/csv"
)