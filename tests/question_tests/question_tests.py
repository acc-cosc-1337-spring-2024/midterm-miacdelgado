#write function tests here, don't add input('') statements here!
import unittest

# Since there was only one test files I wrote out all the test cases in here. Whenever I want to test it
# I just temporarily delete or comment out the lines I don't want to run. 


# Question A Test Cases
from src.question_a.question_a import get_random_number

class Test_Config(unittest.TestCase):
    def test_question_a_test_1(self):
        self.assertEqual("The number guessed is larger. Try again.", get_random_number(1))
    def test_question_a_test_2(self):
        self.assertEqual("The number guess is smaller. Try again.", get_random_number(3))
    def test_question_a_test_3(self):
        self.assertEqual("You guessed the correct number!", get_random_number(5))

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