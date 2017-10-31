#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from pymongo import MongoClient
from bson import json_util
import os
client = MongoClient("localhost",28000)
db=client.movies
films_collection = db.films_one_by_one
for filename in os.listdir("movies-json"):
    movie_json = open("/movies-json/"+filename,"rU")
    film = json_util.loads(movie_json.read())
    films_collection.insert_one(film)


print ("____________________________---------start-display from bd-------")
for film in films_collection.find():
    print(film) # iterate the cursor
print ("____________________________--------end--one-by-one-----")
