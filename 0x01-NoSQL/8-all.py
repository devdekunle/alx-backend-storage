#!/usr/bin/env python3
"""
Module that contains the function that lists all the documents in a
collection
"""
from pymongo import MongoClient

def list_all(mongo_collection):
    """
    lists all documents in a collection
    """
    documents = mongo_collection.find()
    return documents if documents else []
    
