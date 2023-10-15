const express = require('express');
const app = express();
const MongoClient = require('mongodb').MongoClient
const url = 'mongodb://rootadmin:rootpassword@mongo_service:27017/'
const dbName = 'grades_analytics'

const MONGO_URI = "mongodb://rootadmin:rootpassword@mongo_service:27017/";
const MONGO_DB_NAME = "analytics_results";
const MONGO_COLLECTION_NAME = "grades_analytics";

app.set('view engine', 'ejs');

app.get('/statistics', async (req, res) => {
  try {
    // Connect to MongoDB
    const mongoClient = new MongoClient(MONGO_URI, { useNewUrlParser: true, useUnifiedTopology: true });
    await mongoClient.connect();
    
    const db = mongoClient.db(MONGO_DB_NAME);
    const collection = db.collection(MONGO_COLLECTION_NAME);
    
    // Fetch statistics data from MongoDB
    const analytics = await collection.findOne({}, { projection: { _id: 0 } });
    
    // Render a web page with the statistics
    res.render('statistics', { analytics });
    
    // Close the MongoDB connection
    mongoClient.close();
  } catch (error) {
    console.error(error);
    res.status(500).send('Error fetching statistics data');
  }
});

app.listen(5004, () => {
  console.log('Express app is running on http://localhost:5004');
});