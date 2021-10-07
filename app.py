from flask import Flask, render_template
import requests
import xml.etree.ElementTree as ET

def read_url():
    link = 'http://www.ynet.co.il/Integration/StoryRss2.xml'
    response = requests.get(link)
    xml_data = response.text.encode('utf-8', 'ignore') 
    tree = ET.parse(xml_data)
    root = tree.getroot()
    return xml_data

app = Flask(__name__)
@app.route("/")
def main():
    return render_template('index.html')

if __name__ == "__main__":
    #print(read_url())
    app.run()