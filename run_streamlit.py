import streamlit as st
from input import config
from input.config_logging import get_logger
from main import main

logger = get_logger(__name__)

def run():
    st.set_page_config(page_title=config.APP_NAME, page_icon=":chart_with_upwards_trend:")
    st.title(f"{config.APP_NAME} - v{config.APP_VERSION}")
    logger.info("Application started.")
    main()

if __name__ == "__main__":
    run()
