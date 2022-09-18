// JavaScript code to generate HTML files, by reading data from database.

// Gettein required modules
var mysql = require('mysql');
const fs = require('fs')

var connection = mysql.createConnection({
    host: "localhost",
    database: "sample",
    user: "root",
    password: "password",
    multipleStatements: true
});

// Connecting to database
connection.connect();

// Executing database query to get data
connection.query('SELECT * FROM table_name', function (error, results, fields) {

    if (error) throw error;

    // # Initializing loop to get db data in variable
    for (var key in results) {
        
        // Opening a new file with name equal to id and writing the HTML in it. 
        fs.writeFile("Folder path to store HTML files" + (results[key].id) + ".html", "Paste your HTML code here", (err) => {
            if (err) throw err;
        })

        // Printing result
        console.log("File name"+results[key].id+" created successfully!!");
        // console.log(results[key].name);
    }
});
// Ending the SQL connection
connection.end();
