import streamlit as st
import pandas as pd
import plotly.express as px
st.set_page_config(
    page_title="Maven Ski Shop Analytics Dashboard",
    page_icon="🏂",
    layout="wide",
    initial_sidebar_state="expanded")
data = pd.read_excel("maven_ski_shop_data.xlsx",sheet_name="Inventory_Levels")
st.title("Inventory Levels")
col1,col2,col3 = st.columns(3)
col1,col2,col3 = st.columns([3,3,3])
with col1:
    figg = px.pie(data,values="Product_ID",names="Quantity_in_stock",title="Product vs Stock",color_discrete_sequence=px.colors.sequential.RdBu)
    st.plotly_chart(figg)
with col2:
    figure = px.bar(data,x="Product_ID", y="Quantity_in_stock",title="Product vs Quantity",color_discrete_sequence=px.colors.sequential.RdBu)
    st.plotly_chart(figure)
with col3:
    fig = px.histogram(data,x="Product_ID", y="Quantity_in_stock",title="Number of Products in stock",color_discrete_sequence=px.colors.sequential.RdBu)
    st.plotly_chart(fig)
    