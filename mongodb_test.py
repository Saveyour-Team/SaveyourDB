import pymongo

#mydb is independent database
conn = pymongo.MongoClient();
conn.database_names()

collection = db.saveyour
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
