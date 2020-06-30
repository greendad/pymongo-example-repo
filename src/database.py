from pymongo import MongoClient

def singleton(cls):
    instances = {}

    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper
  
@singleton
class Database:
  db = None
  client = None
  
  def __init__(self):
    self.client = MongoClient("mongodb://localhost:27017/test_db")
    self.db = self.client["test_db"]
    
  def get_db(self):
    return self.db