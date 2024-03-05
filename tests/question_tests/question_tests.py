#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_b.question_b import get_day_of_week

class Test_Config(unittest.TestCase):

    def test_question_b_test_1(self):
        self.assertEqual('Invalid Number', get_day_of_week(0))
    def test_question_b_tes_2(self):
        self.assertEqual('Monday', get_day_of_week(1))
    def test_question_b_test_3(self):
        self.assertEqual('Tuesday', get_day_of_week(2))
    def test_question_b_test_4(self):
        self.assertEqual('Wednesday', get_day_of_week(3))
    def test_question_b_test_5(self):
        self.assertEqual('Invalid Number', get_day_of_week(8))

