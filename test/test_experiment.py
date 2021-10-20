"""
09/29/2021
init,
test_retrieve_lexicons, test_is_definition_exists, test_is_lexicon_exists_2
"""

import unittest
from experiment.singleton import Singleton


class TestSingleton(unittest.TestCase):

    def test_init(self):
        s1 = Singleton()
        s2 = Singleton()
        if id(s1) == id(s2):
            print("Same")
        else:
            print("Different")

    def test_print(self):
        s1 = Singleton()
        s2 = Singleton()
        s1.print_test()
        s2.print_test()