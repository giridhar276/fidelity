
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


st.title("Education vs Income Heatmap")
st.sidebar.header("Options")
use_education_num = st.sidebar.radio("Education dimension", ["education", "educational_num"], index=0)
normalize = st.sidebar.checkbox("Normalize rows", value=False)
top_k = st.sidebar.slider("Top K education categories (by count)", 3, 16, 10, 1)

if use_education_num == "education":
    cats = df["education"].value_counts().head(top_k).index.tolist()
    dff = df[df["education"].isin(cats)]
    pivot = pd.crosstab(dff["education"], dff["income"])
else:
    pivot = pd.crosstab(df["educational_num"], df["income"])

if normalize:
    pivot = pivot.div(pivot.sum(axis=1), axis=0).round(3)

st.dataframe(pivot)
fig, ax = plt.subplots()
im = ax.imshow(pivot.values, aspect="auto")
ax.set_xticks(range(pivot.shape[1])); ax.set_xticklabels(pivot.columns, rotation=0)
ax.set_yticks(range(pivot.shape[0])); ax.set_yticklabels(pivot.index)
ax.set_title("Education vs Income")
for i in range(pivot.shape[0]):
    for j in range(pivot.shape[1]):
        ax.text(j, i, str(pivot.values[i, j]), ha="center", va="center", fontsize=8)
fig.colorbar(im, ax=ax)
st.pyplot(fig)
