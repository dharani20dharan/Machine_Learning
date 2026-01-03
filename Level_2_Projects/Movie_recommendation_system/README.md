# Movie Recommendation System

A content-based movie recommendation system that suggests movies similar to a user-selected movie. Built using the TMDB 5000 Movie Dataset and Streamlit.

## 📌 Project Overview
This system uses machine learning techniques to analyze movie metadata (genres, keywords, cast, crew, overview) and recommend top 5 similar movies. It relies on **Cosine Similarity** to measure the closeness between movie tags.

## 📂 Dataset
The project uses the **TMDB 5000 Movie Dataset**:
- `tmdb_5000_movies.csv`: Contains movie details like title, overview, genres, keywords, budget, etc.
- `tmdb_5000_credits.csv`: Contains cast and crew information.

## 🛠️ Tech Stack
- **Python**
- **Pandas, NumPy** (Data Manipulation)
- **Scikit-learn** (Feature Extraction & Similarity Calculation)
- **NLTK/Ast** (Text Processing)
- **Streamlit** (Web Application Interface)
- **Pickle** (Model Serialization)

## ⚙️ How It Works
1. **Data Preprocessing**:
   - Merges movies and credits datasets.
   - Extracts relevant features: `genres`, `keywords`, `cast`, `crew`, `overview`.
   - Cleans and formats textual data (removing spaces, handling JSON formats).
   - Creates a unified `tags` column for each movie.

2. **Vectorization**:
   - Converts text tags into vectors using `CountVectorizer`.
   - Computes **Cosine Similarity** matrix to find relationships between movies.

3. **Recommendation**:
   - Takes a movie title as input.
   - Finds the top 5 most similar movies based on similarity scores.

4. **Web App**:
   - A user-friendly interface built with **Streamlit**.
   - Displays recommendations along with movie posters (fetched via TMDB API or placeholders).

## 🚀 How to Run
1. Install dependencies:
   ```bash
   pip install pandas numpy scikit-learn streamlit
   ```
2. Run the Jupyter Notebook `TMDB_recommmendation_system.ipynb` to generate the model files (`movie_list.pkl`, `similarity.pkl`).
3. Place the `.pkl` files in a `model/` directory.
4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## 📸 Features
- **Dropdown Search**: Select any movie from the database.
- **Visual Recommendations**: Shows movie titles and posters.
- **Offline/Online Mode**: Handles poster fetching with fallbacks if API or path is missing.
