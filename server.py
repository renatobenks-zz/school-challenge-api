from flask import Flask, url_for
from api import Routes

app = Flask(__name__)

@ app.route("/api/v1/<argument>/")
def get(argument):
    return Routes.get(argument)

@ app.route("/api/v1/issue/<id>/")
def getIssue(id):
    return Routes.issue(id)\

@ app.route("/api/v1/question/<id>/")
def getQuestion(id):
    return Routes.question(id)

if __name__ == "__main__":
    app.run('localhost', 5000, debug=True)