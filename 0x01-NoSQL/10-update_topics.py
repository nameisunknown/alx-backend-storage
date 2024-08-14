#!/usr/bin/env python3

"""
This function chnges all topics of a school doc
"""


def update_topics(mongo_collection, name, topics):
    """
    Args:
        mongo_collection: This is a PyMongo collection obj
        name: this is a string
        topics: this is a collection of topics
    """

    filter = {"name": name}
    update_value = {"$set": {"topics": topics}}
    mongo_collection.update_one(filter, update_value)
