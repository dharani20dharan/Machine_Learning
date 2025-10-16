# SLP vs MLP — Breast Cancer Classification

## Overview
This project compares a **Single Layer Perceptron (SLP)** and a **Multi Layer Perceptron (MLP)** on the [Breast Cancer Wisconsin Diagnostic Dataset](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_breast_cancer.html).

Although MLPs are typically more powerful, this dataset is highly structured and nearly linearly separable, making it ideal to demonstrate a real-world scenario where a simpler linear model can perform on par with or better than a neural network.

---

## Tech Stack
- Python 3.x  
- scikit-learn  
- NumPy & Pandas  
- Matplotlib & Seaborn

---

## Features
- Load and preprocess dataset with feature scaling  
- Train and evaluate both SLP and MLP models  
- Measure performance using accuracy and F1-score  
- Visualize confusion matrices  
- Summarize performance in a comparison table

---

## Model Performance

| Metric          | SLP (Perceptron) | MLP (Neural Network) |
|-----------------|------------------|------------------------|
| Accuracy        | 98.25%           | 97.66%                 |
| F1-Score        | 98.60%           | 98.11%                 |

**Key Insight:**  
- The dataset’s features allow linear separation with minimal error.  
- The SLP model, despite its simplicity, slightly outperformed the MLP.  
- MLP did not surpass SLP because there was little non-linear structure to learn from.

---
