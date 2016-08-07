import unittest
from api.modules.words import words

words.Words.words = [
        {'id': 1, 'questions_id_question': 1, 'issues_id_issue': 1, 'word': 'gordos', 'characters': 6},
        {'id': 2, 'questions_id_question': 2, 'issues_id_issue': 1, 'word': 'pizza', 'characters': 5},
        {'id': 3, 'questions_id_question': 2, 'issues_id_issue': 1, 'word': 'pizza de chocolate', 'characters': 18},
        {'id': 4, 'questions_id_question': 1, 'issues_id_issue': 1, 'word': 'pizza de banana', 'characters': 18},
        {'id': 5, 'questions_id_question': 2, 'issues_id_issue': 1, 'word': 'pizza de merda', 'characters': 18}
    ]

class Words(unittest.TestCase):
    def testCharactersIsRight(self):
        words.choiceWords(2, None)
        for word in words.Words.choicedWords:
            self.assertEqual(word['characters'], len(word['word']))

    def testIfGiveMeWordsWithAllParams(self):
        words.choiceWords(2, 1)
        self.assertEqual(len(words.Words.choicedWords), 3)

    def testResponseWords(self):
        words.Words.words = [
            {'id': 2, 'questions_id_question': 2, 'issues_id_issue': 1, 'word': 'pizza', 'characters': 5},
            {'id': 3, 'questions_id_question': 2, 'issues_id_issue': 1, 'word': 'pizza de chocolate', 'characters': 18},
        ]
        words.choiceWords(2, 1)
        self.assertEqual(words.Words.choicedWords, words.Words.words)

    def testIfDontPassNothing(self):
        words.choiceWords(None, None)
        self.assertEqual(len(words.Words.choicedWords), 0)

    def testIfEverResponseWithOneObject(self):
        words.choiceWords(2, 1)
        word = [words.shuffleWords(words.Words.choicedWords)]
        self.assertEqual(len(word), 1)

    def testIfResponseOfShuffleWordsIsInWords(self):
        words.choiceWords(2, 1)
        word = words.shuffleWords(words.Words.choicedWords)
        self.assertEqual(word['word'], words.Words.words[word['id']-1]['word'])
