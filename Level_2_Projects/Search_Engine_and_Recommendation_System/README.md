# Search Engine and Product Recommendation System

A search engine capability built on the **Amazon Product Dataset**, allowing users to search for products and receive recommendations based on text similarity.

## 📌 Project Overview
This project implements an information retrieval system that matches user search queries with product titles and descriptions. It leverages **Natural Language Processing (NLP)** techniques like Stemming and TF-IDF Vectorization to compute similarity scores and rank results.

## 📂 Dataset
- **Amazon Product Dataset (`amazon_product.csv`)**: Contains product information including:
  - `Title`: Name of the product.
  - `Description`: Detailed description of the product.
  - `Category`: Categorization of the item.

## 🛠️ Tech Stack
- **Python**
- **Pandas, NumPy** (Data Handling)
- **NLTK (Natural Language Toolkit)** (Tokenization & Stemming)
- **Scikit-learn** (TF-IDF Vectorization & Cosine Similarity)
- **Streamlit** (Web Interface)

## ⚙️ Methodology
1. **Text Preprocessing**:
   - **Tokenization**: Breaking down text into individual words using `nltk.word_tokenize`.
   - **Stemming**: Reducing words to their root form (e.g., "running" -> "run") using `SnowballStemmer`.
   - Concatenating `Title` and `Description` to create a rich feature set (`stemmed_tokens`).

2. **Feature Extraction**:
   - Uses **TF-IDF (Term Frequency-Inverse Document Frequency)** to convert text data into numerical vectors, highlighting important words while downplaying common ones.

3. **Similarity Calculation**:
   - Computes **Cosine Similarity** between the user's query vector and product vectors.
   - Sorts products by similarity score in descending order.

4. **Web Application**:
   - A **Streamlit** app provides an interactive search bar.
   - Displays the top 10 matching products along with their descriptions and categories.

## 🚀 How to Run
1. Install dependencies:
   ```bash
   pip install pandas numpy nltk scikit-learn streamlit
   ```
2. Ensure you have the `amazon_product.csv` file in the directory.
3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## 📸 Features
- **Smart Search**: Matches synonyms and root words (e.g., searching for "running shoes" finds "run shoe").
- **Top 10 Results**: Instantly retrieves the most relevant items.
- **Clean UI**: Simple interface for easy usage.
