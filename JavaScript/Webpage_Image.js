// JavaScript code to take screenshot of a webpage and saving it as an image

// Getteing required modules
const puppeteer = require('puppeteer');

// Writing whole code in async
(async () => {
    // Setting page quality/dimensions
    const browser = await puppeteer.launch({
        defaultViewport: { width: 3840, height: 2160 }
    });
    // Opening the browser
    const page = await browser.newPage();
    // Opening the given link
    await page.goto("https://www.google.com/", { waitUntil: 'domcontentloaded' });
    // Setting path to store the captured image
    let a = "path to store created image" + ".png";
    // Capturing the webpage as an image.
    await page.screenshot({ path: a });
    // Closing the browser
    await browser.close();
})();
