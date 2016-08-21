db.test.aggregate(

  // Pipeline
  [
    // Stage 1
    {
      $match: {
      	artDate:{
      	  $gte:new Date(2015/12/1),
      	  $lt:new Date(2015/12/31)
      	}
      }
    },

    // Stage 2
    {
      $unwind: "$topic_sentiment_total"
    },

    // Stage 3
    {
      $group: {
      	_id:{year: {$year: "$artDate"}, month: {$month: "$artDate"},day:{$dayOfMonth: "$artDate"}},
      	total:{ $sum:"$topic_sentiment_total.sentiment_count" }
      }
    },

    // Stage 4
    {
      $project: {
      	date: {
           year: "$_id.year",
           month:"$_id.month",
           day:"$_id.day"
           },
           total:1,
           _id:0
      }
    },

    // Stage 5
    {
      $sort: {
      	 "_id.day":1
      }
    }

  ]

  // Created with 3T MongoChef, the GUI for MongoDB - http://3t.io/mongochef

);
