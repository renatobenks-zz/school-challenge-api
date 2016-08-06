import unittest
from api.modules.questions import questions

class Issues(unittest.TestCase):
    def testQuantityQuestions(self):
        self.assertGreaterEqual(len(questions.question), 3)
    def testResultQuestionsList(self):
        pass