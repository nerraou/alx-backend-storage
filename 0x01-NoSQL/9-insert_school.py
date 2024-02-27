#!/usr/bin/env python3
""" 9-insert_school """
from pymongo.collection import Collection


def insert_school(mongo_collection: Collection, **kwargs):
    """ insert school """
    record = mongo_collection.insert_one(kwargs)
    return record.inserted_id
