from AnimalShelter import AnimalShelter
from bson.objectid import ObjectId

AAC = AnimalShelter("accuser", "accuser123")


######################
""" Creating Data """"
######################


#Creating data to be added into database
data = [{
    "name": "Katie",
    "type": "dog"
}, {
    "name": "Emily",
    "type": "dog"
}, {
    "name": "Alan",
    "type": "cat"
}]

#For loop for adding data to database
for i in data:
    AAC.create(i)


####################
""" Reading Data """
####################


#Reading the data that we jsut added to the database
dogs = AAC.read({"type": "dog"})
cats = AAC.read({"type": "cat"})

for dog in dogs:
    print(dog)
for cat in cats:
    print(cat)


#####################
""" Updating Data """
#####################

#Selecting data inserted into database to update document and add outcome_type 
updateAAC = AAC.update({"name": "Alan"}, {"outcome_type": "Transfer"})
print(updateAAC)

#Searching for updated document
search = AAC.read({"name": "Alan"})
for animal in search:
    print(animal)


#####################
""" Deleting Data """
#####################


#Deleting document from database 
deleteAAC = AAC.delete({"name": "Alan"})
print()deleteAAC

#Searching for document to verify deletion from database 
search = AAC.read({"name": "Alan"})
for animal in search:
    print(animal)
