from api.modules.issues import issues

question = ['What is obviously about this?', 'What is beauty about this?', 'What is most important for this?']
questions = []

for i, issue in enumerate(issues.issues):
    questions.append({
            'id_question': (i + 1),
            'issue_id_issue': issue['id_issue'],
            'question': question[i]
        })