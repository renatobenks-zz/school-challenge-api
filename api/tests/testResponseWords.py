import unittest
from api import Routes


class getResponseWord(unittest.TestCase):
    def testTypeResponse(self):
        self.assertEqual(type(Routes.getResponseWord(Routes, 'pizza', 'z')), dict)

    def testLenResponse(self):
        self.assertEqual(len([Routes.getResponseWord(Routes, 'pizza', 'z')]), 1)

    def testWhatIsResponse(self):
        mock = {
            'isValid': True,
            'quantity': 2
        }
        self.assertDictEqual(Routes.getResponseWord(Routes, 'pizza', 'z'), mock)

    def testFieldsType(self):
        self.assertEqual(type(Routes.getResponseWord(Routes, 'pizza', 'z')['isValid']), bool)
        self.assertEqual(type(Routes.getResponseWord(Routes, 'pizza', 'z')['quantity']), int)
