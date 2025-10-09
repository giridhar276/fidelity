
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


st.title("Demographic Breakdown")
st.sidebar.header("Filters")
races = st.sidebar.multiselect("Race", options=sorted(df["race"].dropna().unique()), default=[])
genders = st.sidebar.multiselect("Gender", options=sorted(df["gender"].dropna().unique()), default=[])
stack_by = st.sidebar.radio("Stack by", ["income", "gender", "race"], index=0)
group_axis = st.sidebar.radio("Group axis", ["race", "gender", "education", "workclass"], index=0)

dff = df.copy()
if races: dff = dff[dff["race"].isin(races)]
if genders: dff = dff[dff["gender"].isin(genders)]

ct = pd.crosstab(dff[group_axis], dff[stack_by])
st.dataframe(ct)

st.subheader(f"Stacked Bar: {group_axis} vs {stack_by}")
fig, ax = plt.subplots()
cumulative = np.zeros(len(ct))
for col in ct.columns:
    ax.bar(ct.index, ct[col], bottom=cumulative, label=str(col))
    cumulative += ct[col].values
ax.set_xlabel(group_axis); ax.set_ylabel("Count"); ax.legend(title=stack_by)
ax.set_xticklabels(ct.index, rotation=45, ha="right")
st.pyplot(fig)
