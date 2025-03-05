from pymongo import MongoClient

def connect_db():
    try:
        client=MongoClient("")