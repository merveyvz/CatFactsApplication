import requests
from datetime import datetime
from database import Session
from models import CatFact
from config import CAT_FACTS_API_URL, CAT_IMAGE_API_URL
from sqlalchemy.sql.expression import func
import random

# Fetch cat facts from the API and save them to the database
def fetch_and_save_cat_facts():
    session = Session()
    response = requests.get(CAT_FACTS_API_URL)
    facts = response.json()
    new_facts_count = 0
    for fact in facts:
        existing_fact = session.query(CatFact).filter_by(fact_id=fact['_id']).first()
        # Create a new CatFact object and add it to the session if it does not exist
        if not existing_fact:
            new_fact = CatFact(
                fact_id=fact['_id'],
                text=fact['text'],
                created_at=datetime.strptime(fact['createdAt'], "%Y-%m-%dT%H:%M:%S.%fZ"),
                updated_at=datetime.strptime(fact['updatedAt'], "%Y-%m-%dT%H:%M:%S.%fZ"),
                verified=fact['status']['verified']
            )
            session.add(new_fact)
            new_facts_count += 1

    # Commit the session to save the new facts to the database
    session.commit()
    session.close()
    return new_facts_count


def get_random_cat_fact_and_image():
    session = Session()
    fact = session.query(CatFact).order_by(func.random()).first()
    session.close()

    if fact:
        # Add a random query parameter to bypass caching
        image_url = f"{CAT_IMAGE_API_URL}?random={random.randint(1, 1000000)}"
        return fact, image_url
    return None, None
