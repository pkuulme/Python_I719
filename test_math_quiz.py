import unittest
import quiz
from quiz import Quiz


class OutcomeTest(unittest.TestCase):
    def test_amount(self):
        q = Quiz()
        self.assertEqual(len(q.questions),5)



if __name__ == '__main__':
    unittest.main()