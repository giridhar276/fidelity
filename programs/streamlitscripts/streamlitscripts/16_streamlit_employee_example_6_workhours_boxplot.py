
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


st.title("Work Hours Insights")
st.sidebar.header("Controls")
cat = st.sidebar.radio("Categorical split", ["marital_status","relationship","workclass","gender","race"], index=0)
min_age = st.sidebar.slider("Minimum age", int(df["age"].min()), int(df["age"].max()), int(df["age"].min()))
show_outliers = st.sidebar.checkbox("Show underlying points", value=False)

dff = df[df["age"] >= min_age].copy()
order = dff[cat].value_counts().index.tolist()

st.subheader(f"Hours/Week by {cat}")
fig, ax = plt.subplots()
data = [dff.loc[dff[cat]==val, "hours_per_week"] for val in order]
ax.boxplot(data, labels=order, vert=True, showfliers=show_outliers)
ax.set_ylabel("Hours per Week"); ax.set_xlabel(cat)
ax.set_title(f"Distribution of Hours per Week by {cat} (Age >= {min_age})")
st.pyplot(fig)

st.dataframe(dff[[cat, "hours_per_week", "age"]].head(200))
