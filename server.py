from flask import Flask, url_for, make_response, jsonify, request, abort
from api import Routes
from api.modules.words import words

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

@ app.route("/api/v1/word", methods=['POST'])
def getWord():
    if not request.json:
        abort(400)
    Words = Routes.word(Routes, request.json['id_question'], request.json['id_issue'])
    if Words:
        return jsonify({
            'word': words.shuffleWords(Words)
        })

@ app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == "__main__":
    app.run('localhost', 5000, debug=True)