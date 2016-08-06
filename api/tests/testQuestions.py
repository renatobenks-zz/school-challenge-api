import unittest
from api import getQuestion, Routes
from api.modules.questions import questions

class Questions(unittest.TestCase):
    def testNotResponseForNotExistQuestion(self):
        self.assertEqual(Routes.question(4), None)
    def testResponseForExistQuestion(self):
        self.assertEqual(getQuestion(1), questions.questions[0])
