#  CO₂ Emission Prediction using Regression Models

This project demonstrates how various regression techniques can be applied to predict **CO₂ emissions** based on engine and vehicle parameters.  
The goal is to compare the performance of different models — from simple to advanced — and determine which one best fits the data.

---

##  Models Implemented

1. **Simple Linear Regression**  
2. **Multiple Linear Regression**  
3. **Polynomial Regression (Degree = 2)**  
4. **Ridge Regression**  
5. **Lasso Regression**

---

##  Technologies Used

- Python 3.x  
- NumPy  
- Pandas  
- Matplotlib  
- Scikit-learn  

---

##  Workflow

1. **Data Preprocessing:**  
   - Loaded dataset and selected relevant features.  
   - Handled missing values and scaled numerical data where necessary.

2. **Model Training:**  
   - Trained each regression model on the dataset.  
   - Optimized parameters for Ridge and Lasso to avoid overfitting.

3. **Evaluation:**  
   - Used **Mean Squared Error (MSE)** and **R² Score** as performance metrics.  
   - Compared results across models to identify the best-performing one.

---

##  Model Performance

| Model                     | Mean Squared Error (MSE) | R² Score |
|----------------------------|--------------------------|-----------|
| Simple Linear Regression   | 949.99                   | 0.7238    |
| Multiple Linear Regression | 422.04                   | 0.8773    |
| Polynomial Regression (Deg=2) | 272.03                | 0.9209    |
| Ridge Regression           | 422.04                   | 0.8773    |
| Lasso Regression           | 422.06                   | 0.8773    |

---

##  Summary

Among all models tested, **Polynomial Regression (Degree = 2)** performed the best,  
achieving the **lowest Mean Squared Error (≈ 272.03)** and the **highest R² Score (≈ 0.92)**.  
This indicates that there is a **non-linear relationship** between engine parameters and CO₂ emissions.  

**Multiple Linear Regression** also performed well (R² ≈ 0.88), offering a **simpler and more interpretable** alternative with slightly lower accuracy.

---


