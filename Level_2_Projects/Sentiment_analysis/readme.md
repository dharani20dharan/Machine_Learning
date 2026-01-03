# Amazon Product Review Sentiment Analysis

This project implements a **searchable sentiment analysis system** on an Amazon product review dataset using both **VADER** and **RoBERTa** pretrained models. It provides insights into customer feedback, visualizes sentiment distributions, and compares rule-based and transformer-based sentiment scoring.

## Features
- Exploratory Data Analysis (EDA) on review scores.
- Tokenization, POS tagging, and named entity recognition using **NLTK**.
- Sentiment scoring with **VADER** for quick polarity estimation.
- Advanced sentiment scoring with **RoBERTa** transformer model.
- Comparative analysis between VADER and RoBERTa scores.
- Visualization of positive, neutral, and negative sentiments per review score.
- Pipeline integration for quick sentiment prediction on new text.

## Technologies
- Python, Pandas, Numpy
- NLTK
- Matplotlib, Seaborn
- Transformers (Hugging Face)
- PyTorch

## Usage
1. Load the dataset (`Reviews.csv`).
2. Perform EDA and basic NLP preprocessing.
3. Compute sentiment scores using VADER and RoBERTa.
4. Visualize sentiment distributions and analyze examples.
5. Use the Hugging Face pipeline for fast predictions on new reviews.

## Outcome
- Identifies sentiment trends across review ratings.
- Enables a hybrid sentiment analysis combining rule-based and ML-based approaches.
- Can serve as a foundation for a **search engine or recommendation system** based on review sentiment.
