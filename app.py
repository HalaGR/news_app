from flask import Flask, render_template
import requests


app = Flask(__name__)
@app.route("/")
def main():
    return render_template('index.html')

if __name__ == "__main__":
    # read xml file and save in file.xml in static dir
    data = "http://www.ynet.co.il/Integration/StoryRss2.xml"
    resp = requests.get(data)
    with open('static/file.xml', 'wb') as foutput:
        foutput.write(resp.content)
    # run app
    app.run()