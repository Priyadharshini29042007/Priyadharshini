import os
from flask import Flask
app=Flask(__name__)
@app.route("/")
def home():
    return "welcome priya"

@app.route("/about")
def about():
    return "welcome to auxilium college" 

if __name__=="__main__":
    app.run(host="0.0.0.0" ,port="5000")
    