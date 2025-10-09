
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


st.title("Grouped Statistics Explorer")
st.sidebar.header("Settings")
group_by = st.sidebar.radio("Group by", options=["education", "workclass", "gender", "marital_status", "occupation", "race", "native_country", "income"], index=0)
agg_target = st.sidebar.multiselect("Numeric metrics", options=["age","fnlwgt","educational_num","capital_gain","capital_loss","hours_per_week"], default=["age","hours_per_week"])
top_n = st.sidebar.slider("Show Top N groups (by size)", 5, 30, 12, 1)

if agg_target:
    sizes = df[group_by].value_counts().head(top_n).index.tolist()
    dff = df[df[group_by].isin(sizes)].copy()
    stats = dff.groupby(group_by)[agg_target].mean().round(2).sort_values(agg_target[0], ascending=False)
    st.dataframe(stats)

    st.subheader("Group Sizes")
    counts = dff[group_by].value_counts().sort_values(ascending=True)
    fig, ax = plt.subplots()
    counts.plot(kind="barh", ax=ax)
    ax.set_xlabel("Count"); ax.set_ylabel(group_by); ax.set_title(f"Top {top_n} {group_by} by Count")
    st.pyplot(fig)
else:
    st.info("Pick at least one metric to aggregate.")



