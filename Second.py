from pymongo import MongoClient

client=MongoClient('mongodb://localhost:27017')

print (client)

db=client.library #db name

collection=db["Books"] #collection name

#dictionary

Students=[
  { "id": 1, "name": "John", "address": "Highway 37"},
  { "id": 2, "name": "Peter", "address": "Lowstreet 27"},
  { "id": 3, "name": "Amy", "address": "Apple st 652"},
  { "id": 4, "name": "Hannah", "address": "Mountain 21"},
  { "id": 5, "name": "Michael", "address": "Valley 345"},
  { "id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
  { "id": 7, "name": "Betty", "address": "Green Grass 1"},
  { "id": 8, "name": "Richard", "address": "Sky st 331"},
  { "id": 9, "name": "Susan", "address": "One way 98"}
  ]
x = collection.insert_many(Students)

dblist = client.list_database_names()
if input('Enter database name :.') in dblist:
    print("The database exists.")
else:
    print("Not Present")
print(dblist)

for x in collection.find(): #for finding all occurences in collection
    print(x)

print(Students)