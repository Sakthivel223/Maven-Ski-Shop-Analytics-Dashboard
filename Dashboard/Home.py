import streamlit as st

st.set_page_config(
    page_title="Maven Ski Shop Analytics Dashboard",
    page_icon="🏂",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🏂 Maven Ski Shop Analytics Dashboard")
st.markdown("---")

st.subheader("Welcome!")
st.write(
    """
    This is a multi-page analytics dashboard for **Maven Ski Shop**, built using **Streamlit** 📊.
    
    Use the **sidebar navigation** to explore:
    
    - 📄 Product Info: Metrics and price breakdown
    - 📦 Inventory Levels: Stock insights and visualizations
    - 🧾 Orders Info: Sales, tax, and customer analytics
    """
)
st.image("https://www.shutterstock.com/image-vector/quick-descent-against-backdrop-sky-260nw-2434366881.jpg", use_container_width=True)


