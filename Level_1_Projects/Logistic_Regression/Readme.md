# Machine Learning Classification Projects

This repository contains two classification projects demonstrating **Logistic Regression** with real-world datasets:

1. **Titanic Survival Prediction** – Predicts passenger survival using categorical and numerical features.  
2. **Iris Species Classification** – Classifies Iris flower species using multinomial logistic regression.

---

## Project 1: Titanic Survival Prediction

### Overview
- **Goal:** Predict whether a Titanic passenger survived.  
- **Dataset:** `titanic` dataset from Seaborn.  
- **Target Classes:**  
  - 0 = Did not survive  
  - 1 = Survived  

- **Techniques Used:**  
  - Logistic Regression (Base, L1, L2 regularization)  
  - Confusion Matrix & ROC Curve  
  - Feature encoding and handling missing data  

###  Workflow
1. Data preprocessing: handle missing values and encode categorical features.  
2. Split data into training and testing sets.  
3. Train Logistic Regression models with L1 and L2 regularization.  
4. Evaluate models using **accuracy**, **classification report**, **confusion matrix**, and **ROC curve**.  
5. Visualize feature importance and regularization effects.  

### Model Performance

| Model | Accuracy | Notes |
|-------|----------|-------|
| Base Logistic Regression | ~80% | Balanced bias-variance |
| L1 Regularization (Lasso) | ~79% | Performs feature selection |
| L2 Regularization (Ridge) | ~80% | Improves coefficient stability |

### Summary
All models achieve around **80% accuracy**.  
- **L1 Regularization** reduces less important features, useful for feature selection.  
- **L2 Regularization** stabilizes coefficients and reduces overfitting.  
- Logistic Regression provides a strong, interpretable baseline for binary classification problems.

---

## Project 2: Iris Species Classification

### Overview
- **Goal:** Classify Iris flower species (`Setosa`, `Versicolor`, `Virginica`).  
- **Dataset:** Iris dataset from `sklearn.datasets` (150 samples, 4 features).  
- **Techniques Used:**  
  - Multinomial Logistic Regression (softmax)  
  - Feature scaling with `StandardScaler`  
  - PCA for 2D visualization  
  - Cross-validation  

###  Workflow
1. Feature scaling for better convergence.  
2. Train multinomial logistic regression model on scaled features.  
3. Reduce features to 2D using PCA for visualization.  
4. Evaluate model using **confusion matrix**, **classification report**, and **cross-validation**.  
5. Visualize decision boundaries using PCA-reduced data.  

###  Model Performance
- Confusion matrix and classification report show **high accuracy** for all three classes.  
- Cross-validated accuracy: ~97%  
- PCA plot demonstrates clear class separation in 2D space.

### Summary
Multinomial Logistic Regression achieves near-perfect classification.  
- Feature scaling improves model convergence.  
- PCA allows interpretable visualization of decision boundaries.  
- Cross-validation confirms robustness and generalization.

---

##  Technologies Used

- Python 3.x  
- Pandas, NumPy  
- Matplotlib, Seaborn  
- Scikit-learn  

---
