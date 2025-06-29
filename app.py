import streamlit as st
import numpy as np
import pickle

# Load Trained Kmeans Model
kmeans = pickle.load(open("kmeans.pkl", 'rb'))

# Simple clustering function
def clustering(Amount, Frequency, Recency):
    new_customer = np.array([[Amount, Frequency, Recency]])
    predicted_cluster = kmeans.predict(new_customer)

    if predicted_cluster[0] == 0:
        return "New/Infrequent Shoppers"
    elif predicted_cluster[0] == 1:
        return "Loyal Regulars"
    else:
        return "High-Value/Big Spenders"

# Streamlit app here
st.title("Customer Clustering App")
st.write("Enter the customer details:")

# User input (side by side inputs)

# Row 1 with two columns
col1, col2 = st.columns(2)
with col1:
    st.subheader("Enter Total amount of money spent (0-15000)")
    amount = st.number_input("Amount", min_value=0, max_value=15000, value=0)  # Changed to 'amount'

with col2:
    st.subheader("Enter Number of purchases (0-750)")
    frequency = st.number_input("Frequency", min_value=0, max_value=750, value=0)  # Changed to 'frequency'

# Row 2 with two columns
col1, col2 = st.columns(2)
with col1:
    st.subheader("Enter Days since last purchase (0-400)")
    recency = st.number_input("Recency", min_value=0, max_value=400, value=0)  # Changed to 'recency'

# Predict button
if st.button("Predict Cluster"):
    cluster_label = clustering(amount, frequency, recency)  # Pass updated variable names
    st.success(f'The customer belongs to the "{cluster_label}" cluster.')
