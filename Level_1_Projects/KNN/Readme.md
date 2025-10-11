# Wine Classification using K-Nearest Neighbors (KNN)

This project implements a K-Nearest Neighbors (KNN) classifier to predict wine types based on their chemical attributes. It demonstrates model training, evaluation, and distance metric comparison using the **Wine dataset**.

---

## Dataset
- **Source:** Built-in `load_wine()` dataset from `sklearn`
- **Samples:** 178
- **Features:** 13 chemical properties of wine
- **Target Classes:** 3 wine cultivars

---

## Machine Learning Workflow

1. **Load Dataset**
   - Used `load_wine()` from `sklearn.datasets`.
   - Converted data into pandas DataFrame for easier handling.

2. **Data Preprocessing**
   - Checked for missing values.
   - Scaled features using `StandardScaler`.
   - Stratified train-test split for balanced class representation.

3. **Model Training**
   - Trained `KNeighborsClassifier` with **K=3**.
   - Explored accuracy across different values of K (1–20).

4. **Model Evaluation**
   - Accuracy: `97.22%`
   - Best distance metric: **Manhattan** (100% accuracy)
   - Evaluated using:
     - Accuracy Score
     - Classification Report
     - Confusion Matrix

5. **Visualization**
   - Plotted accuracy scores for different K values to identify optimal K.

---

## Results

| Metric                    | K=3 (Euclidean) | Manhattan |
|---------------------------|------------------|-----------|
| Accuracy                  | 97.22%           | 100.00%   |
| Misclassifications        | 1                | 0         |
| Best Performing Metric    | —                | ✅        |

### Classification Report (K=3)

| Class | Precision | Recall | F1-score | Support |
|-------|-----------|--------|----------|---------|
| 0     | 0.92      | 1.00   | 0.96     | 12      |
| 1     | 1.00      | 0.93   | 0.96     | 14      |
| 2     | 1.00      | 1.00   | 1.00     | 10      |

### Confusion Matrix

[[12 0 0]
[ 1 13 0]
[ 0 0 10]]

---

## Tech Stack

-  Python
-  scikit-learn
-  pandas, matplotlib
-  numpy

---
