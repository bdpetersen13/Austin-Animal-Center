
# Austin Animal Center

This project combines the python programming language, the NoSQL database solution MongoDB, and the dash web framework to create a full-stack application that provides Austin Animal Center, or AAC for short, with the tools necessary to easily track and analyze both the animals under their care and the outcomes of these animals. 

This project uses CRUD functionality written in python to modify and maintain the MongoDB database. In addition, the dash web framework is used to create a web application that will make it easy for AAC to interact with and analyze the data in the database. 



## Motivation

As its final project, this application was developed for Southern New Hampshire University, SNHU, course CS340: Client/Server Development. The scenario of this project is as follows: 

“As a developer for Global Rain, a software engineering company specializing in custom software, you and your team have been assigned a project working with Grazioso Salvare, an international rescue-animal training company. 

After a meeting with Grazioso Salvare, it has been determined they’re seeking a software application that will work in conjunction with existing data from animal shelters in the Austin, Texas, area. To objective of the application is to identify and categorize available dogs.”

Over the year, AAC will see hundreds of animals coming through their doors needing care. Creating and maintaining a database will help to increase productivity and be more time efficient. As a result, this will allow AAC to put more effort into caring for and treating the animals they’re watching over.  

![image](https://user-images.githubusercontent.com/89234922/184561376-2093d99f-9460-48a1-91ee-77174eb92670.png)


## Installation

To run this project, a variety of tools are needed to be installed before a successful run can be made.

Here is the list of tools being utilized for this project:

•	MongoDB: an open-source NoSQL database architecture

•	Python: an object-oriented programming language

•	pymongo: a python distribution with tools for interacting with MongoDB and its collections

•	Dash: a python framework for creating interactive web applications

•	Jupyter Notebook: An open-source web-based computer platform for running live code

## Getting Started

To get started with this application, the data for AAC will need to be downloaded to the local device. Once downloaded, you will need to open your terminal and traverse to the folder where the data was just downloaded to. Once in the folder you will need to start the MongoDB server.

Here is a sample scripts to do the above steps:

    cd /usr/local/datasets
    /usr/local/bin/mongod_ctl start-noauth


Once the MongoDB server has successfully started, the next step is to create the database and collection and to import the AAC data.

Here is a sample script to do the above step:

    cd  /usr/local/datasets
    /usr/local/bin/mongod_ctl start-noauth

    mongoimport --db AAC --collection animals/animal_shelter_outcomes

    mongo

    show dbs
    use AAC
    use animals


Once the database is created and the data imported, it’s important to verify the data has been imported correctly.

Here is a sample script to pull data from the database:

    db.inspections.updateMany({breed: “Siamese mix”}, {$set: {color: “black/white”}})
    db.animals.createIndex({“breed”: 1, “outcome_type”: 1})
    db.animals.find({breed: “Siamese Mix”}, {outcome_type: “transfer”})
    db.animals.find({breed: “Siamese Mix”}, {outcome_type: “transfer”}).count()

The next step for setting up the database is to create user accounts. Since this application is meant to be used by multiple individuals it’s essential to set up various account for everyone with all of them having corresponding roles and access to the data.

Here is a sample script for creating a new user:

    /usr/local/bin/mongod_ctl stop
    /usr/local/bin/mongod_ctl start
    mongo -authenticationDatabase “admin” -u “admin” -p

    Use admin
    db.createUser({user: “accuser”, pwd: “accuser123”, roles: [{“readWrite”, db: “ACC”}]})


