from flask import Flask
from flask_pymongo import PyMongo

app=Flask(__name__)
app.config["SECRET_KEY"]="9bcff7180b57ea1e51f18de2b568a7e2556d1f5e"
app.config["MONGO_URI"]="mongodb+srv://wardalomar2001:ZWmeiVdCRnmNM97O@cluster0.xwgajlf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

#setup mongo
mongo_client= PyMongo(app)
db=mongo_client.db

from application import routes