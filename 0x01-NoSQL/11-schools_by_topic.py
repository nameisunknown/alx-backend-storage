#!/usr/bin/env python3
"""
this function returns a list of school documents that have the specified topic.
"""


def schools_by_topic(mongo_collection, topic):
    """
    Args:
        mongo_collection: A PyMongo collection object.
        topic: (string) The topic to search for in school documents.
    Returns:
        A list of dictionaries representing the school documents
        that contain the topic.
    """

    filter = {"topics": {"$in": [topic]}}
    schools = list(mongo_collection.find(filter))

    return schools
