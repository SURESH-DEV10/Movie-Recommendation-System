import pandas as np
import streamlit as st
import requests
import pickle


with open('movie_data.pkl', 'rb') as file:
    movies, cosine_sim = pickle.load(file)

def get_recommendation(title, cosine_sim=cosine_sim):
    idx = movies[movies['title'] == title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11] #get top 10 similar movies 
    movie_indices = [i[0] for i in sim_scores]
    return movies[['title', 'id']].iloc[movie_indices]   


def fetch_poster(id):
    api_key = 'dcaa61a285fd0da636e54f18a0003cb2'
    url = f'http://api.themoviedb.org/3/movie{id}?api_key={api_key}'
    response = requests.get(url)
    data = response.json()
    print(data)

    poster_path = data.get('poster_path')
    if not poster_path:
        # Handle missing poster gracefully
        return "https://via.placeholder.com/500x750?text=No+Poster+Available"

    return f"https://image.tmdb.org/t/p/w500{poster_path}"
    # poster_path = data['poster_path']
    #full_path = f"https://image.tmdb.org/t/p/w500{poster_path}"
    #return full_path


st.title("Movie Recommendation System")

selected_movie = st.selectbox("select a movie:", movies['title'].values)

if st.button('Recommend'):
    recommendations = get_recommendation(selected_movie)
    st.write("Top 10 movies:")

    # create a 2*5 grid layout
    for i in range(0, 10, 5):  #loop over rows(2 rows, 5 movies each)
        cols = st.columns(5)   # create 5 columns for each row
        for col, j in zip(cols, range(i, i+5)):
            if j < len(recommendations):
                movies_title = recommendations.iloc[j]['title']
                poster_url = fetch_poster(id)
                with col:
                    st.image(poster_url, width=130)
                    st.write(movies_title)