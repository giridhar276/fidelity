
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


st.title("Capital Gains & Losses Analyzer")
st.sidebar.header("Filters")
gain_min, gain_max = st.sidebar.slider("Capital Gain range", int(df["capital_gain"].min()), int(df["capital_gain"].max()), (0, int(df["capital_gain"].max())))
loss_min, loss_max = st.sidebar.slider("Capital Loss range", int(df["capital_loss"].min()), int(df["capital_loss"].max()), (0, int(df["capital_loss"].max())))
age_min, age_max = st.sidebar.slider("Age range", int(df["age"].min()), int(df["age"].max()), (int(df["age"].min()), int(df["age"].max())))
income_choice = st.sidebar.radio("Income", options=["(All)"] + sorted(df["income"].dropna().unique().tolist()))

filtered = df[(df["capital_gain"].between(gain_min, gain_max)) &
              (df["capital_loss"].between(loss_min, loss_max)) &
              (df["age"].between(age_min, age_max))].copy()
if income_choice != "(All)":
    filtered = filtered[filtered["income"] == income_choice]

st.subheader("Age vs Hours per Week (colored by Income)")
fig, ax = plt.subplots()
colors = {"<=50K": "tab:blue", ">50K": "tab:orange"}
for inc, sub in filtered.groupby("income"):
    ax.scatter(sub["age"], sub["hours_per_week"], s=10, alpha=0.6, label=str(inc),
               c=[colors.get(inc, "tab:gray")])
ax.set_xlabel("Age"); ax.set_ylabel("Hours per Week")
ax.legend(title="Income")
st.pyplot(fig)

st.subheader("Capital Gain vs Capital Loss")
fig2, ax2 = plt.subplots()
ax2.scatter(filtered["capital_gain"], filtered["capital_loss"], s=8, alpha=0.5)
ax2.set_xlabel("Capital Gain"); ax2.set_ylabel("Capital Loss")
st.pyplot(fig2)

st.dataframe(filtered.head(200))
