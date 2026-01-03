#  Amazon Product Recommendation System

Content-based recommendation engine for **Amazon products** using NLP and cosine similarity.

---

##  Overview
- Cleaned and preprocessed product data (`amazon_product.csv`)  
- Tokenized and stemmed titles & descriptions using **NLTK SnowballStemmer**  
- Computed **TF-IDF** vectors for product texts  
- Measured **cosine similarity** between query and product descriptions  
- Returns top 10 most relevant products for a given search query  

