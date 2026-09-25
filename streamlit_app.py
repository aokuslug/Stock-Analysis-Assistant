import streamlit as st

st.set_page_config(
    page_title="Stock Analysis Assistant",
    layout="wide"
)

st.title("Stock Analysis Assisstant")

st.write (
    "Research US-listed stocks using technical, fundamental, "
    "and market data."
)

ticker = st.text_input(
    "Enter a stock ticker",
    placeholder="Example:AAPL"
)

if st.button("Analyze"):
    if ticker:
        st.success(f"Selected stock: {ticker.upper()}")
    else:
        st.warning("Please enter a stock ticker.")
