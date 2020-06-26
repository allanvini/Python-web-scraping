

from flask import Flask

import json



import scraper



app = Flask(__name__)



@app.route("/news",methods=["GET"]) #O GET já é por padrão, não precisaria, mas deixei por ser mais semântico



def home():

    scraper.run

    with open("news.json") as file_object:

        newsJSON = json.load(file_object)

    data = json.dumps(newsJSON)

    return str(data), 200



if (__name__ == "__main__"):

    app.run(debug = True)

