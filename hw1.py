from pymongo import MongoClient
from pymongo import errors
import datetime

# mongoURI = "mongodb://%s:%s@%s/%s?authMechanism=SCRAM-SHA-1" % (ACCOUNT, PW, IP, DB)
mongoURI = 'mongodb://localhost:27017/'

try:
    client = MongoClient(mongoURI)
    # client = MongoClient('localhost', 27017)
    # print(client.server_info())
    db = client.db_class
except errors.ConnectionFailure as err:
    print(err)

results = db.test.aggregate([
  {
      "$unwind": "$artLike"
    },
    {
      "$group": {
      	"_id":"$artTitle",
      	"total":{"$sum":{ "$add": [ "$artLike.FBLike", "$artLike.GoogleLike" ] }},
      }
    },
    {
      "$sort": {
      	"total":-1
      }
    },
    {
      "$limit": 10
    }
])

for each_result in results:
    print(each_result)