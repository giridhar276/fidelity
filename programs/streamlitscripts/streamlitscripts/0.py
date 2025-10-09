import streamlit as st

st.title("this is the app title")
st.markdown("this is the markdown")
st.header("this is the header")
st.subheader("this is the subheader")
st.caption("this is the caption")

st.code("x=2021", language="python")

# LaTeX (raw string with triple quotes, like in the screenshot)
st.latex(r"""
a + a r ^{1} + a r^{2} + a r^{3}
""")
