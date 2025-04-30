import streamlit as st
from input import config

def render_sidebar_inputs():
    st.sidebar.header("Input Parameters")
    pre_money = st.sidebar.number_input("Pre-money Valuation ($)", value=config.DEFAULT_PRE_MONEY_VALUATION)
    new_investment = st.sidebar.number_input("New Investment ($)", value=config.DEFAULT_NEW_INVESTMENT)
    existing_shares = st.sidebar.number_input("Existing Shares", value=config.DEFAULT_EXISTING_SHARES)
    return pre_money, new_investment, existing_shares

def render_results(post_money, share_price, new_shares, existing_pct, new_pct):
    st.header("Dilution Results")
    st.metric("Post-money Valuation", f"${post_money:,.2f}")
    st.metric("New Share Price", f"${share_price:,.4f}")
    st.metric("New Shares Issued", f"{new_shares:,.0f}")
    st.subheader("Ownership Distribution")
    st.write(f"Existing Shareholders: {existing_pct:.2f}%")
    st.write(f"New Investors: {new_pct:.2f}%")