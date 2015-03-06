import pymongo

#mydb is independent database
conn = pymongo.MongoClient('ec2-54-173-26-10.compute-1.amazonaws.com', 22, ssl=True, ssl_keyfile='simran.pem')
db = conn.mydb
db
conn.database_names()

collection = db.my_collection
collection
db.collection_names()

print('Going to create some new documentes');

#create a simple document
def newUser(login, usrname, pwd):
    doc = {"name": usrname, "login": login, "password":pwd}
    collection.insert(doc)


newUser("ssd@saveyour.com", "ssd1", "pwd1");
newUser("john@saveyour.com", "j1", "pwd2");
print('We created some new documents');
print('Some of our db information');
print(conn.database_names());
print(db.collection_names());
print('ok bye');
