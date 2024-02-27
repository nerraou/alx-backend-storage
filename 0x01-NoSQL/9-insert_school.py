#!/usr/bin/env python3
""" 9-insert_school """
from pymongo.collection import Collection


def insert_school(mongo_collection: Collection, **kwargs: dict):
    """ insert school """
    return mongo_collection.insert_one(kwargs)
