import unittest
from api.modules.words import responseWord

response = responseWord.Response


class ResponseWords(unittest.TestCase):
    def testResponseValidLetterIsABoolean(self):
        self.assertEqual(type(response.validLetter(response, 'pizza', 'z')['isValid']), bool)

    def testResponseIsTrue(self):
        self.assertEqual(response.validLetter(response, 'pizza', 'p')['isValid'], True)

    def testResponseIsFalse(self):
        response.isValid = {'isValid': False, 'quantity': 0}
        self.assertEqual(response.validLetter(response, 'pizza', 't')['isValid'], False)

    def testResponseIsTrueIfLetterExistTwice(self):
        self.assertEqual(response.validLetter(response, 'pizza', 'z')['isValid'], True)

    def testIfIsNoneTheTimesThanShowLetter(self):
        response.isValid = {'isValid': False, 'quantity': 0}
        response.validLetter(response, 'pizza', 't')
        self.assertEqual(response.isValid['quantity'], 0)

    def testTwiceThanShowLetter(self):
        response.validLetter(response, 'pizza', 'z')
        self.assertEqual(response.isValid['quantity'], 2)

    def testOneThanShowLetter(self):
        response.validLetter(response, 'pizza', 'i')
        self.assertEqual(response.isValid['quantity'], 1)

    def testHowMuchTimesShowLetters(self):
        response.validLetter(response, 'pizzzzzzza', 'z')
        self.assertEqual(response.isValid['quantity'], 7)

    def testIfIsAOnlyResultInArray(self):
        self.assertEqual(len([response.isValid]), 1)
