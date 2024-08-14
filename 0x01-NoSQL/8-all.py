#!/usr/bin/env python3

"""
This module lists all documents in a PyMongo collection
"""


def list_all(mongo_collection):
    """
    Args:
        mongo_collection: this is a PyMongo collection

    Returns:
        This func retirns an empty list if no docs are found
        and returns a list of dict if found
    """

    docs = list(mongo_collection.find())
    return docs
