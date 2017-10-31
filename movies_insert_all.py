# -*- coding: utf-8 -*-
from pymongo import MongoClient
from bson import json_util
client = MongoClient("localhost",28000)
db=client.movies
films_collection = db.films_all
#films_collection.delete_many({})
movies_json = open("movies.json","rU")
films = json_util.loads(movies_json.read())
print ("------------------insertion --in--bd----------------")
for film in films:
    films_collection.insert_one(film)
print ("----------------end--insert---------------")


print ("____________________________---------start-display from bd-------")
for film in films_collection.find():
    print(film) # iterate the cursor
print ("____________________________--------end---------")