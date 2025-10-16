# Breast Cancer Classification using SVM

## Project Overview
This project demonstrates the application of Support Vector Machines (SVM) for classifying breast cancer as malignant or benign using the Breast Cancer Wisconsin dataset. Two kernel approaches are compared:
- Linear SVM
- RBF (Radial Basis Function) SVM

Additionally, PCA is applied to visualize decision boundaries in 2D space.

## Tech Stack
- Python
- scikit-learn
- NumPy, Pandas
- Matplotlib, Seaborn

## Workflow
1. **Data Loading**: Load the breast cancer dataset from scikit-learn.
2. **Data Preprocessing**: Train-test split and feature scaling.
3. **Model Training**: Linear and RBF SVM models trained on the scaled data.
4. **Evaluation**: Accuracy, classification report, and confusion matrix.
5. **PCA Visualization**: Dimensionality reduction and decision boundary visualization.

## Results
- Linear SVM Accuracy: 95.6%
- RBF SVM Accuracy: 98.2%
- RBF model outperformed linear due to its ability to capture non-linear patterns.
