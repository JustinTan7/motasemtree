// init-mongodb.js

// Connect to the MongoDB instance
var conn = new Mongo();
var db = conn.getDB("analytics_results");

// Check if the grades analytics collection exists
if (!db.getCollectionNames().includes("grades_analytics")) {
    // Create the grades analytics collection
    db.createCollection("grades_analytics");

    // Initialize data
    var lowestGrade = 0;
    var highestGrade = 0;
    var averageGrade = 0;

    // Insert initial data into the collection
    db.grades_analytics.insert({
        "Lowest Grade": lowestGrade,
        "Highest Grade": highestGrade,
        "Average Grade": averageGrade
    });
}
