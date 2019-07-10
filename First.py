#for single record 

from pymongo import MongoClient

client=MongoClient('mongodb://localhost:27017')

print (client)

db=client.library #db name

collection=db["Books"] #collection name

book={}

book["title"]="Anatomy"

book["year"]=1997

book["author"]="rahim"

collection.insert_one(book)

print(book)

cursor=collection.find()

print(book['title'])

print(book['year'])

dblist = client.list_database_names()
if input('Enter DB') in dblist:
    print("The database exists.")
else:
    print("Not Present")

print(dblist)
