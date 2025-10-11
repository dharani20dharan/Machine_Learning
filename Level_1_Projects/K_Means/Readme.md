# Customer Segmentation using K-Means Clustering

This project applies **K-Means Clustering** to segment customers based on their **Annual Income** and **Spending Score**.  
It enables businesses to identify distinct customer groups and tailor marketing strategies accordingly.

---

## Project Overview

The goal of this project is to perform **unsupervised learning** to understand customer behavior patterns.  
By segmenting customers into clusters, businesses can:

- Target high-spending customers more effectively  
- Design personalized marketing campaigns  
- Optimize product offerings and pricing strategies

---

## Methodology

1. **Data Loading:**  
   Imported the `Mall_Customers.csv` dataset containing customer demographics and spending behavior.

2. **Feature Selection:**  
   Selected two key features:
   - `Annual Income (k$)`
   - `Spending Score (1-100)`

3. **Data Scaling:**  
   Standardized features using `StandardScaler` to ensure fair distance calculations.

4. **Optimal K Selection:**  
   Applied the **Elbow Method** to determine the ideal number of clusters (`K = 5`).

5. **Model Training:**  
   Trained the K-Means algorithm with `n_clusters=5`.

6. **Cluster Visualization:**  
   Plotted customer segments and centroids to understand group separation visually.

7. **Cluster Analysis:**  
   Calculated average income and spending score for each cluster.

---

## Cluster Insights

| Cluster | Annual Income (k$) | Spending Score (1-100) | Description                             |
|---------|---------------------|-------------------------|------------------------------------------|
| 0       | 55.30               | 49.52                   | Average income & moderate spenders       |
| 1       | 86.54               | 82.13                   | High income & high spenders (premium)   |
| 2       | 25.73               | 79.36                   | Low income but high spenders (youth)    |
| 3       | 88.20               | 17.11                   | High income & low spenders (conservative)|
| 4       | 26.30               | 20.91                   | Low income & low spenders (budget)      |

---

## Results

- **Optimal clusters:** 5  
- **Segmentation:** Customers are grouped into distinct clusters based on purchasing power and spending behavior.  
- **Visualization:** Clear separation between high-value and low-value segments.

---

## Technologies Used

- **Python**
- **Pandas**, **NumPy**
- **Matplotlib**, **Seaborn**
- **Scikit-learn**

---
