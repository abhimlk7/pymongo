from pymongo import MongoClient

client=MongoClient('mongodb://localhost:27017')

print (client)

db=client.library #db name

collection=db["Books"]

client.drop_database("library")   #for droping the db
print(client.list_database_names())