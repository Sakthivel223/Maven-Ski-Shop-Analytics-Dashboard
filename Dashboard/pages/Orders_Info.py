import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt
st.set_page_config(
    page_title="Maven Ski Shop Analytics Dashboard",
    page_icon="🏂",
    layout="wide",
    initial_sidebar_state="expanded")
st.title("Orders Info")
df = pd.read_excel("maven_ski_shop_data.xlsx",sheet_name="Orders_Info")
unique_customers = df["Customer_ID"].nunique()
total = df["Total"].sum()
average_tax = df["Tax"].mean()
highest_subtotal = df["Subtotal"].max()
col1,col2,col3,col4 = st.columns(4)
with col1:
    st.metric(label="Number of Customers",value=unique_customers)
with col2:
    st.metric(label="Total Sales(USD)",value=f"${total:.2f}")
with col3:
    st.metric(label="Average Tax(USD)",value=f"${average_tax:.2f}")
with col4:
    st.metric(label="Highest Subtotal(USD)",value=f"${highest_subtotal:.2f}")
col1, col2 = st.columns(2)
col1,col2 =st.columns([3,3])
with col1:
    f = alt.Chart(df).mark_line().encode(
        x="Customer_ID",
        y="Tax"
    ).properties(title="Analysis of Customer ID vs Tax")
    st.altair_chart(f,use_container_width=True)
with col2:
    figure = alt.Chart(df).mark_bar().encode(
        x="Customer_ID",
        y="Total"
    ).properties(title="Analysis of Customer ID vs Total")
    st.altair_chart(figure,use_container_width=True)
with st.container():
    figgg = px.box(df,x="Order_ID",y="Total",title="Analysis of Order ID vs Total")
    st.plotly_chart(figgg)
with st.container():
    figuree = px.scatter(df,x="Location",y="Total",title="Total by Location")
    st.plotly_chart(figuree)
