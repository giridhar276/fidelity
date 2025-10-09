
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

@st.cache_data
def load_data():
    df = pd.read_csv("employee.csv")
    return df

df = load_data()
st.caption("Dataset shape: {} rows, {} columns".format(df.shape[0], df.shape[1]))


st.title("Employee Overview Dashboard")
st.sidebar.header("Filters")
workclass = st.sidebar.multiselect("Workclass", options=sorted(df["workclass"].dropna().unique()), default=[])
education = st.sidebar.multiselect("Education", options=sorted(df["education"].dropna().unique()), default=[])
gender = st.sidebar.multiselect("Gender", options=sorted(df["gender"].dropna().unique()), default=[])
income = st.sidebar.multiselect("Income", options=sorted(df["income"].dropna().unique()), default=[])

filtered = df.copy()
if workclass: filtered = filtered[filtered["workclass"].isin(workclass)]
if education: filtered = filtered[filtered["education"].isin(education)]
if gender: filtered = filtered[filtered["gender"].isin(gender)]
if income: filtered = filtered[filtered["income"].isin(income)]

col1, col2, col3, col4 = st.columns(4)
col1.metric("Employees", len(filtered))
col2.metric("Avg Age", round(filtered["age"].mean(), 1) if not filtered.empty else 0)
col3.metric("Avg Hours/Week", round(filtered["hours_per_week"].mean(), 1) if not filtered.empty else 0)
col4.metric("Capital Gain > 0", int((filtered["capital_gain"]>0).sum()) if not filtered.empty else 0)

st.subheader("Age Distribution")
fig, ax = plt.subplots()
ax.hist(filtered["age"], bins=20)
ax.set_xlabel("Age"); ax.set_ylabel("Count"); ax.set_title("Histogram of Age")
st.pyplot(fig)

st.subheader("Top Occupations")
top_occ = (filtered["occupation"].value_counts().head(15)).sort_values(ascending=True)
fig2, ax2 = plt.subplots()
top_occ.plot(kind="barh", ax=ax2)
ax2.set_xlabel("Count"); ax2.set_ylabel("Occupation"); ax2.set_title("Top Occupations (Filtered)")
st.pyplot(fig2)

st.subheader("Sample Records")
st.dataframe(filtered.head(100))
