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
      "$unwind": "$topic_sentiment_total"
    },
    {
      "$group": {
      	"_id":{"year": {"$year": "$artDate"}, "month": {"$month": "$artDate"},"day":{"$dayOfMonth": "$artDate"}},
      	"total":{ "$sum":"$topic_sentiment_total.sentiment_count" }
      }
    },
    {
      "$project": {
      	"date": {
           "year": "$_id.year",
           "month":"$_id.month",
           "day":"$_id.day"
           },
           "total":1,
           "_id":0
      }
    },
    {
      "$sort": {
      	 "date.day":1
      }
    }
])

for each_result in results:
    print(each_result)