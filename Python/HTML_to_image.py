# Python code to convert HTML to an image.

# Importing required libraries
from html2image import Html2Image

# Variable declaration
img = Html2Image()

# Assigning whole HTML to a variable 
html = "<!doctype html><html lang='en'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width, initial-scale=1'><link href='node_modules/bootstrap/dist/css/bootstrap.min.css' rel='stylesheet'><title>Bootstrap demo</title></head><body><div style='width:3840px; height:2160px; background-color: #DDD; position: relative;'><div style='position: absolute; top:0; left:0; background-color:  white; height: 410px; width: 100%;'><text style='font-size: 200px; position: relative; color: #000000; top: 100px;left: 100px;'>What Color Is ?</text></div><div style='position: absolute; top:410px; left:0; background-color:  BLUE; height: 1750px; width: 100%;'><text style='font-size: 200px; color: aquamarine; position: relative; top: 60px;left: 100px;'>BLUE</text></div></div></body></html>"

# Converting HTML to an image(.png form)
img.screenshot(html_str=html, save_as='sample.png')
