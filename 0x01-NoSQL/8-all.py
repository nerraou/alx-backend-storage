#!/usr/bin/env python3
""" 8-all """


def list_all(mongo_collection):
    """ list all documents """
    return mongo_collection.find()
