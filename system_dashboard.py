
import streamlit as st
import pandas as pd

# Load CSV file


@st.cache_data
def load_data():
    return pd.read_csv("combined_symptoms.csv")


df = load_data()

# Sidebar filters
st.sidebar.title("Filters")
selected_categories = st.sidebar.multiselect(
    "Filter by category:",
    options=df["category"].unique(),


search_term=st.sidebar.text_input("Search symptoms:")

# Apply filters
filtered_df=df[df["category"].isin(selected_categories)]

if search_term:
    filtered_df=filtered_df[filtered_df["symptom"].str.contains(
        search_term, case=False, na=False)]

# Display results
st.title("Symptom Comparison Dashboard")
st.write(f"Showing {len(filtered_df)} symptoms")

st.dataframe(filtered_df)

# Optional: show shared symptoms
if st.checkbox("Show symptoms shared across categories"):
    freq=df.groupby("symptom")["category"].nunique().reset_index()
    shared=freq[freq["category"] > 1]
    st.subheader("Overlapping Symptoms")
    st.dataframe(shared)
