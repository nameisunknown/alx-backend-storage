#!/usr/bin/env python3

"""
This module inserts a new doc into a colection
based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """
    Args:
        mongo_collection: this is a PyMongo collection object
        **kwargs: This is a dict containg mapped values
    Returns:
        this returns an objectId of the newly inserted docs
    """

    school_doc_tobereturned = mongo_collection.insert_one(kwargs)
    return school_doc_tobereturned.inserted_id

