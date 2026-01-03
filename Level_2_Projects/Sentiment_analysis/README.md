# Sentiment Analysis on Amazon Reviews

A comprehensive sentiment analysis project comparing rule-based approaches (**VADER**) with deep learning techniques (**RoBERTa**) to analyze customer feedback.

## 📌 Project Overview
The goal of this project is to classify Amazon reviews into positive, neutral, or negative sentiments. It explores the limitations of traditional \"Bag of Words\" models and demonstrates the superiority of Transformer-based models in capturing context and sarcasm.

## 📂 Dataset
- **Amazon Fine Food Reviews (`Reviews.csv`)**: Contains over 500,000 reviews with:
  - `Id`: Review ID.
  - `Score`: Rating between 1 and 5.
  - `Summary`: Brief summary of the review.
  - `Text`: The full review content.

## 🛠️ Tech Stack
- **Python**
- **Pandas, NumPy** (Data Analysis)
- **Matplotlib, Seaborn** (Visualization)
- **NLTK (Natural Language Toolkit)** (Text Preprocessing & VADER)
- **Transformers (Hugging Face)** (RoBERTa Model)
- **PyTorch** (Deep Learning Backend)
- **SciPy** (Matrix Operations)

## ⚙️ Methodology
1. **Exploratory Data Analysis (EDA)**:
   - Visualizing distribution of review scores.
   - Analyzing review length and keyword frequency.

2. **VADER (Valence Aware Dictionary and sEntiment Reasoner)**:
   - A rule-based sentiment analysis tool tuned for social media text.
   - Computes `Previous`, `Neutral`, `Negative`, and `Compound` scores.
   - **Pros**: Fast, no training required.
   - **Cons**: Ignores word order and context (e.g., \"not good\" might be misjudged).

3. **RoBERTa (Robustly Optimized BERT Approach)**:
   - A pre-trained Transformer model (`cardiffnlp/twitter-roberta-base-sentiment`).
   - Fine-tuned on millions of tweets to understand informal language, sarcasm, and slang.
   - **Pros**: Context-aware, highly accurate.
   - **Cons**: Computationally expensive, slower than VADER.

## 📊 Results & Comparison
- **VADER**: Effective for simple sentences but struggles with negation and mixed sentiments having sarcasm.
- **RoBERTa**: Outperformed VADER significantly in capturing nuanced sentiments, accurately detecting negative sentiment even in 3-star reviews that might seem neutral.

## 🚀 How to Run
1. Install dependencies:
   ```bash
   pip install pandas numpy matplotlib seaborn nltk transformers torch scipy tqdm
   ```
2. Download the `twitter-roberta-base-sentiment` model (will happen automatically on first run).
3. Run the Jupyter Notebook `Sentiment_analysis.ipynb` to see the step-by-step analysis and comparisons.
