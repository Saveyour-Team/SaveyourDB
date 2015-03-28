import pymongo
from bson import Binary, Code
from bson.json_util import dumps


class setUserData:

    def __init__(self, usrname, pwd):
        self.u = usrname;
        self.p = pwd;
        conn = pymongo.mongoClient();
        collection = db.SaveYourDB
        print('Connecting to saveyour db')

    
