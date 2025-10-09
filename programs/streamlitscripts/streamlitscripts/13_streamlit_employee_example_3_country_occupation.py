
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


st.title("Country & Occupation Explorer")
st.sidebar.header("Filters")
country = st.sidebar.selectbox("Native Country", options=["(All)"] + sorted(df["native_country"].dropna().unique().tolist()))
occupations = st.sidebar.multiselect("Occupations", options=sorted(df["occupation"].dropna().unique()), default=[])
show_table = st.sidebar.checkbox("Show data table", True)

filtered = df.copy()
if country != "(All)":
    filtered = filtered[filtered["native_country"] == country]
if occupations:
    filtered = filtered[filtered["occupation"].isin(occupations)]

st.subheader("Education Distribution")
edu_counts = filtered["education"].value_counts().sort_values(ascending=True)
fig, ax = plt.subplots()
edu_counts.plot(kind="barh", ax=ax)
ax.set_xlabel("Count"); ax.set_ylabel("Education"); ax.set_title("Education Levels (Filtered)")
st.pyplot(fig)

st.subheader("Age by Gender")
fig2, ax2 = plt.subplots()
for g, sub in filtered.groupby("gender"):
    ax2.hist(sub["age"], bins=20, alpha=0.5, label=str(g))
ax2.set_xlabel("Age"); ax2.set_ylabel("Count"); ax2.set_title("Age Distribution by Gender")
ax2.legend()
st.pyplot(fig2)

if show_table:
    st.dataframe(filtered.head(200))
