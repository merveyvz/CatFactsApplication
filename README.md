# Cat Facts

## 🐱 Description

Cat Facts is an interactive web application that provides users with random cat facts along with adorable cat images. 
Built with Python and Streamlit, this app fetches cat facts from an API, stores them in a SQLite database, and displays them alongside randomly generated cat images.

## ✨ Features

- Fetches and stores cat facts from an external API
- Displays random cat facts with a single click
- Shows a new, cute cat image with each fact
- Database management using SQLAlchemy ORM

## 🚀 Setup and Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/merveyvz/CatFactsApplication.git
2. Install the required packages:
   ```bash
   pip install streamlit sqlalchemy requests
3. Run the Streamlit app:
   ```bash
   streamlit run app.py
4. Open your web browser and go to http://localhost:8501 to view the app.

## 📁 Project Structure

- `app.py`: Main application file
- `cat_facts_service.py`: Services for fetching and managing cat facts
- `config.py`: Configuration settings
- `database.py`: Database connection and initialization
- `models.py`: Database models
- `style.css`: Custom styles for the app

## 👏 Acknowledgements

- Cat facts provided by [Cat Facts API](https://github.com/alexwohlbruck/cat-facts?tab=readme-ov-file)
- Cat images provided by [Cataas](https://cataas.com)
