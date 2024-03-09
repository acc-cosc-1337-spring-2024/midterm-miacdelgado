#write function tests here, don't add input('') statements here!
import unittest


# Question A Test Cases
from src.question_a.question_a import 

class Test_Config(unittest.TestCase):
    def test_question_a_test_1(self):

# Question B Test Cases
from src.question_b.question_b import get_day_of_week

class Test_Config(unittest.TestCase):
    def test_question_b_test_1(self):
        self.assertEqual("Invalid Number", get_day_of_week(0))
    def test_question_b_test_2(self):
        self.assertEqual("Monday", get_day_of_week(1))
    def test_question_b_test_3(self):
        self.assertEqual("Tuesday", get_day_of_week(2))
    def test_question_b_test_4(self):
        self.assertEqual("Wednesday", get_day_of_week(3))
    def test_question_b_test_5(self):
        self.assertEqual("Invalid Number", get_day_of_week(8))

# Question C Test Cases
from src.question_c.question_c import is_prime
  
class Test_Config(unittest.TestCase):
    def test_question_c_test_1(self):
        self.assertEqual(False, is_prime(4))
    def test_question_c_test_2(self):
        self.assertEqual(True, is_prime(5))
    def test_question_c_test_3(self):
        self.assertEqual(True, is_prime(11))

# Question D Test Cases
from src.question_d.question_d import get_person_category

class Test_Config(unittest.TestCase):
    def test_question_d_test_1(self):
        self.assertEqual("Infant", get_person_category(1))
    def test_question_d_test_2(self):
        self.assertEqual("Child", get_person_category(2))
    def test_question_d_test_3(self):
        self.assertEqual("Teenager", get_person_category(14))
    def test_question_d_test_4(self):
        self.assertEqual("Adult", get_person_category(20))