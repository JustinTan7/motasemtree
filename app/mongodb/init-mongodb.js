// init-mongodb.js

// Connect to the MongoDB instance
var conn = new Mongo();
var db = conn.getDB("analytics_results");

// Check if the grades analytics collection exists
if (!db.getCollectionNames().includes("grades_analytics")) {
    // Create the grades analytics collection
    db.createCollection("grades_analytics");
    db.grades_analytics.insertOne({
        "lowest_grade": 0,
        "highest_grade": 100,
        "average_grade": 50
    
    });
    
}
