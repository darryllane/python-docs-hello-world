from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "This Application is a quick example of deploying a custom Python Web Application via Microsoft CDN"
