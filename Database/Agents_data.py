import pymongo
import datetime
import math
import os

def create_id() -> int:
    x = str(datetime.datetime.now())
    l = ["-"," ",":","."]
    for i in x:
        if i in l:
            dl = str(x).split(i)
            
            x = ""
            for j in dl:
                x = x + j
            
    f = int(x) / 1000000000000
    f = str(f)
    f = f.split(".")[1]
    f = int(f)
    return math.floor(f)


def delete_agent_file(agent_id):
    if  os.path.isdir(f"./Backend/Files/{agent_id}"):
        l = os.listdir("./Backend/Files")
        for i in l:
            if agent_id in i:
                os.rmdir(f"./Backend/Files/{i}")
    else:
        print("dir not found")
        
        
# print(create_id())
class AgentsData:
    def __init__(self):
        # self.data = {}
        self.name : str = ""
        try:
            client = pymongo.MongoClient('mongodb://localhost:27017/')
            self.mydb = client["Sahayaka_AI"]
            self.mycol = self.mydb["Agents"]
            
        except pymongo.errors.ServerSelectionTimeoutError as err:
            print(f"Failed to connect to MongoDB: {err}")
        
        
    def get_id(self):
        idd = create_id()
        return idd
    
    def create_agent(self, name):
        d = self.get_id()
        mydict = {"_id": d, "agent_name": name, "chat_history": []}
        x = self.mycol.insert_one(mydict)

        
    def update_name(self, name):
        self.name = name
        
    def get_data(self):
        return self.mycol.find()
    
    def get_data_of(self, agent_id):
        return self.mycol.find({"_id" :  int(agent_id)})
    
    def update_history(self, agent_id, new_his : list):
        self.mycol.update_one({"_id" : int(agent_id)}, { "$set" : {"chat_history" : new_his}})
    
    def delete_history(self, agent_id):
        w = self.get_data_of(agent_id=agent_id)
        for i in w:
            if len(i["chat_history"]) == 0:
                return False
            self.mycol.update_one({"_id" : int(agent_id)}, { "$set" : {"chat_history" : []}})
            return True
        
    def get_name(self):
        return self.name
    
    def delete_all(self):
        self.mycol.delete_many({})
        
    def delete_agent(self, agent_id):
        self.mycol.delete_many({"_id": int(agent_id)})
        delete_agent_file(agent_id=agent_id)


