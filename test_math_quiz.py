import unittest
import datetime
from quiz import Quiz
import quiz


class OutcomeTest(unittest.TestCase):
    def test_print(self):
        self.assertTrue(Quiz.summary, "took")

    def test_time(self):
        self.assertTrue(Quiz.total_correct, int)

if __name__ == '__main__':
    unittest.main()