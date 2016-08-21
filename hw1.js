db.test.aggregate(

  // Pipeline
  [
    // Stage 1
    {
      $unwind: "$artLike"
    },

    // Stage 2
    {
      $group: {
      	_id:"$artTitle",
      	total:{$sum:"$artLike.FBLike"}
      }
    },

    // Stage 3
    {
      $sort: {
      	"total":-1
      }
    },

    // Stage 4
    {
      $limit: 10
    }

  ]

  // Created with 3T MongoChef, the GUI for MongoDB - http://3t.io/mongochef

);
