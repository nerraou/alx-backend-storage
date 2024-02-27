#!/usr/bin/env python3
""" 12-log_stats """
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.logs.nginx

    documents_count = logs_collection.count_documents({})
    get_count = logs_collection.count_documents({"method": "GET"})
    post_count = logs_collection.count_documents({"method": "POST"})
    put_count = logs_collection.count_documents({"method": "PUT"})
    patch_count = logs_collection.count_documents({"method": "PATCH"})
    delete_count = logs_collection.count_documents({"method": "DELETE"})
    path_status_count = logs_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )

    print("{} logs".format(documents_count))
    print("Methods:")
    print("\tmethod GET: {}".format(get_count))
    print("\tmethod POST: {}".format(post_count))
    print("\tmethod PUT: {}".format(put_count))
    print("\tmethod PATCH: {}".format(patch_count))
    print("\tmethod DELETE: {}".format(delete_count))
    print("{} status check".format(path_status_count))
