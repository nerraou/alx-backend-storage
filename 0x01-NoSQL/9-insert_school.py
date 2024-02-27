#!/usr/bin/env python3
""" 9-insert_school """


def insert_school(mongo_collection, **kwargs):
    """ insert school """
    record = mongo_collection.insert_one(kwargs)
    return record.inserted_id
