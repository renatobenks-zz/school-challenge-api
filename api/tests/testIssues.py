import unittest
from api import getIssue, Routes
from api.modules.issues import issues

class Issues(unittest.TestCase):
    def testNotResponseForNotExistIssue(self):
        self.assertEqual(Routes.issue(4), None)
    def testResponseForExistIssue(self):
        self.assertEqual(getIssue(1), issues.issues[0])