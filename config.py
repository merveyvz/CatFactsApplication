# config.py
import os

# Database
DATABASE_URL = 'sqlite:///cat_facts.db'

# API
CAT_FACTS_API_URL = "https://cat-fact.herokuapp.com/facts"
CAT_IMAGE_API_URL = "https://cataas.com/cat"

# UI
PAGE_TITLE = "Cat Facts"
PAGE_ICON = "🐱"
TITLE = "🐱 Cat Facts! 🐱"
WELCOME_MESSAGE = "Welcome to Cat Facts! Click the button below to get a random cat fact."
CSS_FILE = "style.css"

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSS_PATH = os.path.join(BASE_DIR, CSS_FILE)
