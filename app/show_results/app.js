const express = require('express');
const app = express();
const MongoClient = require('mongodb').MongoClient;

const MONGO_URI = "mongodb://rootadmin:rootpassword@mongodb:27017/";
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

    // Retrieve data from MongoDB
    const data = await collection.find({}).toArray();

    // Parse the JSON data to an object
    const jsonData = JSON.parse(JSON.stringify(data[0]));

    // Render the statistics page with the retrieved data
    res.render('statistics', { data: jsonData });

    // Close the MongoDB connection
    mongoClient.close();
  } catch (error) {
    console.error(error);
    res.status(500).send('Error fetching statistics data');
  }
});

app.listen(5004, () => {
  console.log('Express app is running on http://localhost:5004/statistics');
});
