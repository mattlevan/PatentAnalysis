library("jsonlite")
library("ggplot2")
library("rmongodb")

# Load patent data from MongoDB.
mongo <- mongo.create(host = "localhost")
if (mongo.is.connected(mongo) == TRUE) {
  # Get the "patents" db.
  mongo.get.databases(mongo) 
  # Load its collections: ai, all, ml, big_data, data_analysis, prediction.
  colls <- mongo.get.database.collections(mongo, db = "patents")
}


