# 🎬 Movie Recommendation System

Content-based movie recommender using the **TMDB 5000 Movies** dataset.  
Recommends similar movies based on genres, keywords, cast, and crew using **cosine similarity**.

---

## 📁 Project Overview
This project processes and merges movie metadata to generate meaningful content tags for each film and then finds movies similar to a given title.

**Key Steps:**
1. **Data Loading** – Load `tmdb_5000_movies.csv` and `tmdb_5000_credits.csv`.
2. **Data Cleaning & Merging** – Keep essential columns and merge datasets on movie titles.
3. **Feature Engineering** – Extract and clean lists of genres, cast, crew, and keywords.
4. **Text Vectorization** – Convert movie tags into numerical vectors using `CountVectorizer`.
5. **Similarity Computation** – Use **Cosine Similarity** to find and rank similar movies.
6. **Recommendation Function** – Recommend top 5 similar movies for a given title.
7. **Model Persistence** – Save data and similarity matrix using `pickle` for future use.

---

## 🧠 Techniques Used
- **Natural Language Processing (NLP)**
- **Feature Extraction with CountVectorizer**
- **Cosine Similarity for Movie Matching**
- **Data Serialization using Pickle**
