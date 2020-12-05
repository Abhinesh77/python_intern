import  json
x={
    "Name":"aaa",
    "Age":20,
    "city":"xyz",
    "grade": None,
    "result": True,
    "marks1":{"bio":95,"CS":100},
    "marks2":[90,98,99],
    "avg":95.6
}
y=json.dumps(x)
print(y)
print(json.dumps((1,2,3)))
print(json.dumps(list(range(9))))

from pymongo import MongoClient
myclient=MongoClient("mongodb://localhost:27017/") #making connection
db=myclient["ABC"] #database
Collection=db["data"]
with open('D:\\Python Internship\\task12\\data.json') as f:
    file_data=json.load(f)
if isinstance(file_data,list):
    Collection.insert_many(file_data)
else:
    Collection.insert_one(file_data)
