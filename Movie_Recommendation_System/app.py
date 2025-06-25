
import streamlit as st
import pandas as pd
import ast
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the dataset
df = pd.read_csv('dataset/tmdb_5000_movies.csv')
df.dropna(inplace=True)

# Preprocessing
def convert(obj):
    L = []
    for i in ast.literal_eval(obj):
        L.append(i['name'])
    return L[:3]

df['genres'] = df['genres'].apply(convert)
df['keywords'] = df['keywords'].apply(convert)
df['tags'] = df['overview'].apply(lambda x: x.split()) + df['genres'] + df['keywords']
df['tags'] = df['tags'].apply(lambda x: " ".join(x))

# Final filtered dataframe with reset index
new_df = df[['id', 'title', 'tags']].reset_index(drop=True)

# TF-IDF and similarity matrix
tfidf = TfidfVectorizer(max_features=5000, stop_words='english')
vector_matrix = tfidf.fit_transform(new_df['tags'])
similarity = cosine_similarity(vector_matrix)

# Recommendation function
def recommend(movie):
    movie = movie.lower()
    if movie not in new_df['title'].str.lower().values:
        return ["❌ Movie not found. Try a different title."]
    idx = new_df[new_df['title'].str.lower() == movie].index[0]
    distances = similarity[idx]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    return [new_df.iloc[i[0]].title for i in movie_list]

# Streamlit UI
st.set_page_config(page_title="🎬 Movie Recommender")
st.title("🎬 Movie Recommendation System")

selected_movie = st.selectbox("Choose a movie", new_df['title'].sort_values())

if st.button("Recommend"):
    recommendations = recommend(selected_movie)
    st.subheader("📽️ Top 5 Similar Movies:")
    for movie in recommendations:
        st.write("👉", movie)
