#!/usr/bin/env python3
'''Task 8's module.
'''


def list_all(mongo_collection):
    """
    Lists all documents in a collection.

    :param mongo_collection: pymongo collection object
    :return: List of documents or an empty list if no documents are found
    """
    return list(mongo_collection.find())
