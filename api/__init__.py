from flask import jsonify
from api.modules.issues import issues
from api.modules.questions import questions

def getIssue(id):
    for issue in issues.issues:
        if issue['id_issue'] == int(id):
            return issue

def getQuestion(id):
    for question in questions.questions:
        if question['id_question'] == int(id):
            return question

class Routes:
    def get(argument):
        if argument == 'issues':
            return jsonify({
                'issues': issues.issues
            })
        if argument == 'questions':
            return jsonify({
                'questions': questions.questions
            })
        return "<h1>Not found ENDPOINT</h1>"

    def issue(id):
        if getIssue(id):
            return jsonify({
                    'issue': getIssue(id)
                })
        return

    def question(id):
        if getQuestion(id):
            return jsonify({
                    'question': getQuestion(id)
                })
        return