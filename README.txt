# Advanced Clustering Techniques for Customer Segmentation – README

> **Course:** Machine Learning (CSL 7620)
> **Team:** Pooja Naveen Poonia (M24CSA020), Shivani Tiwari (M24CSA029), Suvigya Sharma (M24CSA033)
> **Supervisor:** Dr. Angshuman Paul

---

## Table of Contents

1. [Project Goal](#project-goal)
2. [Dataset](#dataset)
3. [Methodology](#methodology)

   1. [Exploratory Data Analysis](#exploratory-data-analysis)
   2. [Feature Engineering – RFM](#feature-engineering--rfm)
   3. [Clustering Algorithms & Tuning](#clustering-algorithms--tuning)
4. [Results & Insights](#results--insights)
5. [Streamlit App](#streamlit-app)
6. [Key Takeaways](#key-takeaways)


---

## Project Goal

Segment customers of a UK‑based online retailer by purchasing behaviour using unsupervised learning. The clusters support targeted marketing, retention strategies and VIP identification.&#x20;

---

## Dataset

* **Source:** Online Retail (01 Dec 2010 – 09 Dec 2011).
* **Size:** 541, 910 transactions, 8 raw columns (InvoiceNo, StockCode, Description, Quantity, InvoiceDate, UnitPrice, CustomerID, Country).
* **Granularity:** Aggregated to customer‑level for clustering.&#x20;

---

## Methodology

### Exploratory Data Analysis

* **Correlation:** Amount ↔ Frequency highly correlated; Recency largely independent.&#x20;
* **Outliers:** Extreme spenders (> £1.75 M) and super‑frequent buyers detected; mitigated via winsorisation.&#x20;
* **Clusterability:** Hopkins statistic = 0.94 → strong tendency to form clusters.&#x20;

### Feature Engineering – RFM

1. **Recency** – days since last purchase
2. **Frequency** – total transactions
3. **Monetary** – total spend

These derived features capture engagement, loyalty and value.&#x20;

### Clustering Algorithms & Tuning

| Algorithm                 | Optimal Params                   |    Silhouette | Davies‑Bouldin | Notes                                           |
| ------------------------- | -------------------------------- | ------------: | -------------: | ----------------------------------------------- |
| **K‑Means**               | k = 3, *k*-means++               |      **0.51** |           0.74 | Clear elbow; severity of clusters moderate      |
| **MiniBatch K‑Means**     | k = 3, batch = 1022, random init | **0.510 (↑)** |          0.739 | Faster on 540 K rows                            |
| **Gaussian Mixture**      | 4 components, tied covariance    |         0.498 |          0.922 | Chosen via lowest BIC/AIC                       |
| **DBSCAN**                | ε = 0.7, minPts = 5              |         0.686 |              — | Finds 3 clusters + 28 outliers; shape‑agnostic  |
| **Agglomerative (Hier.)** | 2 clusters, complete linkage     | **0.687 (↑)** |       **0.56** | Best compactness/separation overall             |

---

## Results & Insights

* **Cluster Personas** (from K‑Means):

  * *New/Infrequent Shoppers* – recent but low spend & visits.
  * *Loyal Regulars* – moderate spend, frequent purchases.
  * *High‑Value/Big Spenders* – high spend, less frequent.&#x20;
* **Model Comparison:** Hierarchical and MiniBatch K‑Means delivered the strongest structure (Silhouette ≥ 0.51), while GMM captured soft boundaries but at lower separation. DBSCAN excelled at highlighting outliers.&#x20;

---

## Streamlit App

Launch locally:

```bash
streamlit run app.py
```

---

```


---

## Key Takeaways

1. **RFM features are sufficient** to unveil actionable segments in transactional retail data.
2. **Agglomerative Hierarchical** offered the best structural fidelity (Silhouette 0.69, DB 0.56).
3. **MiniBatch K‑Means** balances quality and scalability on 500 K+ rows.
4. **DBSCAN** is valuable for spotting niche or anomalous shoppers that merit bespoke campaigns.
5. An **interactive Streamlit tool** empowers non‑technical stakeholders to iterate on segmentation without code.&#x20;


