import random
class Words:
    words = [
        {'id': 1, 'questions_id_question': 1, 'issues_id_issue': 1, 'word': 'gordos', 'characters': 6},
        {'id': 2, 'questions_id_question': 2, 'issues_id_issue': 1, 'word': 'pizza', 'characters': 5},
        {'id': 3, 'questions_id_question': 2, 'issues_id_issue': 1, 'word': 'pizza de chocolate', 'characters': 18},
    ]
    choicedWords = []

def shuffleWords(words):
    if words:
        return random.choice(words)

def choiceWords(id_question, id_issue):
    choiceWords = []
    for word in Words.words:
        if word not in choiceWords:
            if id_question and id_issue:
                if word['questions_id_question'] == id_question and word['issues_id_issue'] == id_issue:
                    choiceWords.append(word)
    Words.choicedWords = choiceWords
    return shuffleWords(choiceWords)
