#  Customer Segmentation using Gaussian Mixture Models (GMM)

This project performs **customer segmentation** using **Gaussian Mixture Models (GMM)**, allowing businesses to understand customer groups and behaviors more effectively.  

---

##  Dataset  
- **Features:** Customer financial and spending data  
- **Target:** Unsupervised (Clustering)

---

##  Methodology

1. **Data Preprocessing**
   - Dropped `CUST_ID` column
   - Filled missing values with mean
   - Standardized features using `StandardScaler`

2. **Dimensionality Reduction**
   - Applied PCA to reduce features to 2 components for visualization

3. **Model Selection**
   - Used **Silhouette Score** to determine the optimal number of clusters
   - Selected **4 clusters** based on best score

4. **Model Training**
   - Trained **GaussianMixture** model on scaled data

5. **Visualization**
   - Plotted clusters using PCA components

6. **Cluster Summary**
   - Calculated cluster-wise average values to interpret customer segments

---

##  Results

| Cluster | Annual Income (k$) | Spending Score (1-100) |
|---------|---------------------|--------------------------|
| 0       | 55.29               | 49.51                    |
| 1       | 86.53               | 82.13                    |
| 2       | 25.73               | 79.36                    |
| 3       | 88.20               | 17.11                    |
| 4       | 26.30               | 20.91                    |

 **Insight:**  
- Cluster 1 represents high-income, high-spending customers — likely a premium target group.  
- Cluster 3 represents high-income but low-spending customers — a potential upselling segment.

---

##  Tech Stack

-  Python  
-  scikit-learn  
-  pandas, numpy, matplotlib, seaborn  

---
