from api.modules.issues import issues

question = ['What come in your head?', 'What you think is beauty about this?', 'What you think than is most important?']
questions = []

def setQuestionsDefault(index, foreign_key, question):
    return questions.append({
        'id_question': index,
        'issue_id_issue': foreign_key,
        'question': question
    })

for i, issue in enumerate(issues.issues):
    setQuestionsDefault((i + 1), issue['id_issue'], question[i])
