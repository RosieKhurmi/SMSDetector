# Connect to database

from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# List collections
collections = ['spam', 'ham']

# Get MongoDB connection URI and database name from environment variables
MONGO_URI = os.getenv('MONGO_URI')
MONGO_DB = os.getenv('MONGO_DB')

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client[MONGO_DB]


# Get collection name
def get_collection(name):
    return db[name]


# List all collections
def list_collection():
    return db.list_collection_names()
