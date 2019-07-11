from pymongo import MongoClient

client=MongoClient('mongodb://localhost:27017')

print (client)

db=client.library #db name

collection=db["Students"] #collection name

students={}
student_open=True #flag
while student_open:
    
    name=input('enter name of the student:- ' )
    address=input('enter address of the student:- ')
    students[name]=address
    
    repeat=input('do you want to add one more details :- ')
    if repeat=='no':
        student_open=False


for name,address in students.items():
    print(name,address)

x = collection.insert_one(students)

print(students)abh

dblist = client.list_database_names()
if input('Enter database name :.') in dblist:
    print("The database exists.")
else:
    print("Not Present")
    
print(dblist)

for x in collection.find(): #for finding all occurences in collection
    print(x)

