#Importing necessary libraries and modules
from pymongo import MongoClient
from bson.objectid import ObjectId


#############################################
""" CRUD Functionality for AAC Database """
#############################################


class AnimalShelter(object):

    def __init__(self):
        #Initializing the MongoClient to connect the a MongoDB database and collections
        self.client = MongoClient('mongodb://localhost:27017')
        self.database = self.client['project']

    #Create method for the C in CRUD
    def create(self, data):
        #Verifying data criteria was provided and returning exception if not
        if data is not None:
            #Storing results of the insert to a variable
            insert = self.database.animals.insert_one(data)

            #Verifying data was stored
            if insert is not None:
                status = True
            else:
                status = False
            return status
        else:
            raise Exception("Nothing to save because data parameter is empty")

    #Read method for the R in CRUD
    def read(self, data):
        #Verifying search criteria was provided and returning exception if not
        if data is not None:
            animalsCollection = self.database.animals.find(data)
            #return animalsCollection and print cursor
            for animals in animalsCollection:
                print(animals)
        else:
            raise exception("No search criteria provided")

    #Update method for the U in CRUD
    def update(self, data):
        #Verifying the record exists to update and returning exception if not
        if record is not None:
            #Update the documents matching the query criteria and print the number of documents updated
            update_results = self.database.animals.update_many(query, record)
            results = "Documents updated ", json.dumps(
                update_results.modified_count)

            return results
        else:
            raise Exception("Record not found")

    #Delete method for the D in CRUD
    def delete(self, data):
        #Verifying that thre record was successfully deleter and returning exception if not
        if data is not None:
            #Delete the documents mathcing the search criteria
            delete_results = self.database.animals.delete_many(data)
            results = "Documents deleted: " + json.dumps(
                delete_result.deleted_count)

            return results
        else:
            raise Exception("No record provided")
