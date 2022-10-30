''' do not run it with playbutton ,in the terminal type:
cd app_1
streamlit run app.py
to stop service ctrl+c'''


import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

@st.cache
def load_data():
    return pd.read_csv("cps_85_wages.csv")
st.title("streamlit Data App One ")
st.subheader("very easy data analytics in python")
df=load_data()
st.dataframe(df)
st.sidebar.header("select option")

if st.sidebar.checkbox("show Pivot Table Summary"):
    st.subheader("Pivot Table Summary")
    c1,c2=st.columns(2)
    categorical_cols=df.select_dtypes(exclude=np.number).columns
    numeric_cols=df.select_dtypes(include=np.number).columns
    index_cols=c1.select_dtypes("pivot Index",options=categorical_cols)
    values_cols=c1.multiselect("pivot Index",options=numeric_cols)
    func=c1.selectbox("pivot function",options=["mean","sum","count","min","max","std"])
    pivot_df=df.pivot_table(index=index_col,values=values_col,aggfunc=func)
    c2.dataframe(pivot_df)
    for col in values_col:
        fig=px.pie(pivot_df,values=col,nams=pivot_df.index)
        st.plotly_chart(fig)
