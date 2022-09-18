// JavaScript code to take screenshot of a webpage/SQL page and saving it as an image

// Getteing required modules
const puppeteer = require('puppeteer');
const fs = require('fs')

// Declarying path to SQL folder
const dir = "Path_to_SQL_folder"
// Reading directory
const files = fs.readdirSync(dir)
const copyItems = [];

// Pushing each file in the declared array "copyItems"
files.forEach((file) => {
    copyItems.push(file);
});

// Calling function "myFunction" for each file present in the defined directory
copyItems.forEach(myFunction);

// Function for capturing the SQL page as an image.
function myFunction(value, index, array) {
    (async () => {
        // Setting page quality/dimensions
        const browser = await puppeteer.launch({
            defaultViewport: { width: 3840, height: 2160 }
        });
        // Opening the browser
        const page = await browser.newPage();
        // Opening the given link
        await page.goto("file:///(Path_to_SQL_folder)" + value, { waitUntil: 'domcontentloaded' });
        // Setting path to store the captured image
        let a = "path_to_store_created_image" + ".png";
        // Capturing the webpage as an image.
        await page.screenshot({ path: a });
        // Closing the browser
        await browser.close();
    })();
}
