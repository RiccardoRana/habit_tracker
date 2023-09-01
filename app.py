import os
from flask import Flask
from routes import pages
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv() #Per caricare le variabili d'ambiente!

def create_app():
    app=Flask(__name__)
    app.register_blueprint(pages)
    client = MongoClient(os.environ.get("MONGODB_URI"))
    app.db = client.HabitApp
    
    
    return app




















