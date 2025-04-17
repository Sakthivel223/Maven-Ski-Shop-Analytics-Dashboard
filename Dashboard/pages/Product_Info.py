import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt
import openpyxl as xl
wb = xl.load_workbook("maven_ski_shop_data.xlsx")
items = wb["Item_Info"]
inventory = wb["Inventory_Levels"]
orders = wb["Orders_Info"] 
st.set_page_config(
    page_title="Maven Ski Shop Analytics Dashboard",
    page_icon="🏂",
    layout="wide",
    initial_sidebar_state="expanded")
st.title("Product Info")
df = pd.read_excel("maven_ski_shop_data.xlsx",sheet_name="Item_Info")
total_products = df['Product_Name'].nunique()  
average_price = df['Price'].mean()            
highest_price = df['Price'].max()              
lowest_price = df['Price'].min()             

col1, col2, col3, col4 = st.columns(4)
col1, col2, col3, col4 = st.columns([3,3,3,3])
with col1:
    st.metric(label="Total Products", value=total_products)

with col2:
    st.metric(label="Average Price (USD)", value=f"${average_price:.2f}")

with col3:
    st.metric(label="Highest Price (USD)", value=f"${highest_price:.2f}")

with col4:
    st.metric(label="Lowest Price (USD)", value=f"${lowest_price:.2f}")

chart = alt.Chart(df).mark_point().encode(
    x='Product_Name',
    y='Euro Price',
).properties(title="Product vs Euro Price")

scatter_chart = alt.Chart(df).mark_point().encode(
    x='Product_Name',
    y='Price',

).properties(title="Product vs Price")

bar_chart = alt.Chart(df).mark_bar().encode(
    x='Product_Name',
    y='GBP Price',
    ).properties(title = "Product vs GBP Price")

line_chart = alt.Chart(df).mark_line().encode(
    x='Product_Name',
    y='JPY Price'
).properties(title = "Product vs JPY price")
col1, col2, col3, col4 = st.columns(4)
col1, col2, col3, col4 = st.columns([3,3,3,3])
with col1:
    st.altair_chart(scatter_chart, use_container_width=True)
with col2:
    st.altair_chart(bar_chart, use_container_width=True)
with col3:
    st.altair_chart(line_chart, use_container_width=True)
with col4:
    st.altair_chart(chart, use_container_width=True)





