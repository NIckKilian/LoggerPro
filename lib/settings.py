import pymongo

db  =''


class settings():

  def mongoDBconnection(self):
        client = pymongo.MongoClient('mongodb://192.168.1.17:27017/')
        self.db = client.LoggerDB

  def logFileLocations(self):
        collection = self.db['LogSettings']
        settingsList = []
        for x in collection.find():      
          settingsList.append(x)
        return x
        
  def ipBanlist(self):
      pass
