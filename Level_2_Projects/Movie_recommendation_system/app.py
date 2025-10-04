import pickle
import streamlit as st

# ✅ No external API call needed
def fetch_poster(movie_id):
    # If your dataset has a 'poster_path' column, use it:
    try:
        poster_path = movies.loc[movies['movie_id'] == movie_id, 'poster_path'].values[0]
        if isinstance(poster_path, str) and poster_path.strip() != "":
            full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
        else:
            # fallback placeholder
            full_path = "https://via.placeholder.com/500x750?text=No+Poster+Available"
    except:
        # fallback placeholder
        full_path = "https://via.placeholder.com/500x750?text=No+Poster+Available"
    return full_path


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    
    recommended_movie_names = []
    recommended_movie_posters = []

    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names, recommended_movie_posters


# 🎬 Streamlit UI
st.header('🎥 Movie Recommender System (Offline Mode)')
movies = pickle.load(open('model/movie_list.pkl','rb'))
similarity = pickle.load(open('model/similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)

    # ⚠️ beta_columns is deprecated; use columns() instead
    cols = st.columns(5)
    for i, col in enumerate(cols):
        with col:
            st.text(recommended_movie_names[i])
            st.image(recommended_movie_posters[i])
