# app.py
import streamlit as st
from cat_facts_service import get_random_cat_fact_and_image, fetch_and_save_cat_facts
from database import init_db
from config import PAGE_TITLE, PAGE_ICON, TITLE, WELCOME_MESSAGE, CSS_PATH


# Load and apply local CSS file for custom styling
def local_css(file_name):
    with open(file_name, "r") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


def main():
    # Set the page configuration
    st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="centered")
    local_css(CSS_PATH)

    # Display the title and welcome message
    st.title(TITLE)
    st.markdown(WELCOME_MESSAGE)

    # Initialize session state variables for cat fact and image URL
    if 'fact' not in st.session_state:
        st.session_state.fact = None
        st.session_state.image_url = None

    # Button to get a random cat fact
    if st.button("Get a Random Cat Fact"):
        fact, image_url = get_random_cat_fact_and_image()
        if fact:
            st.session_state.fact = fact
            st.session_state.image_url = image_url
        else:
            st.warning("No cat facts available in the database.")

    # Display the cat fact and image if available
    if st.session_state.fact:
        st.markdown(f'<p class="cat-fact">{st.session_state.fact.text}</p>', unsafe_allow_html=True)
        st.image(st.session_state.image_url, caption="A cute cat!", use_column_width=True)


if __name__ == "__main__":
    init_db()
    new_facts_count = fetch_and_save_cat_facts()
    main()
