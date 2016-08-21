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
      $group: {
      	_id:{year: {$year: "$artDate"}, month: {$month: "$artDate"},day:{$dayOfMonth: "$artDate"}},
      	total:{ $sum:1 }
      }
    },

    // Stage 3
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

    // Stage 4
    {
      $sort: {
      	 "_id.day":1
      }
    }

  ]

  // Created with 3T MongoChef, the GUI for MongoDB - http://3t.io/mongochef

);
