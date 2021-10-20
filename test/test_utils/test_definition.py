"""
09/29/2021
init,
test_retrieve_lexicons, test_is_definition_exists, test_is_lexicon_exists_2
"""

import unittest
from utils.definition import DefinitionRetrieverFromWN, DefinitionRetrieverFromDict


class TestDefinitionRetrieverFromWN(unittest.TestCase):

    def test_retrieve_definition(self):
        lex = DefinitionRetrieverFromWN()
        word = "module"
        # print(lex.retrieve_definition("module"))
        self.assertEqual(
            ['one of the inherent cognitive or perceptual powers of the mind', 'detachable compartment of a spacecraft',
             'computer circuit consisting of an assembly of electronic components (as of computer hardware)',
             'a self-contained component (unit or item) that is used in combination with other components'],
            lex.retrieve_definition(word))

    def test_retrieve_definition_2(self):
        lex = DefinitionRetrieverFromWN()
        word = "seed"
        print(lex.retrieve_definition(word))
        self.assertEqual(
            ['a small hard fruit',
             'a mature fertilized plant ovule consisting of an embryo and its food source '
             'and having a protective coat or testa',
             'one of the outstanding players in a tournament',
             'anything that provides inspiration for later work',
             'the thick white fluid containing spermatozoa that is ejaculated by the male '
             'genital tract',
             'go to seed; shed seeds',
             'help (an enterprise) in its early stages of development by providing seed '
             'money',
             'bear seeds',
             'place (seeds) in or on the ground for future growth',
             'distribute (players or teams) so that outstanding teams or players will not '
             'meet in the early rounds',
             'sprinkle with silver iodide particles to disperse and cause rain',
             'inoculate with microorganisms',
             'remove the seeds from'],
            lex.retrieve_definition(word))

    # def test_is_definition_exists(self):
    #     lex = DefinitionRetrieverFromWN()
    #     word = "module"
    #     # print(lex.retrieve_definition("module"))
    #     self.assertEqual(True, lex.is_definition_exists(word))
    #
    # def test_is_definition_exists_2(self):
    #     lex = DefinitionRetrieverFromWN()
    #     word = "module4453"
    #     # print(lex.retrieve_definition("module"))
    #     self.assertEqual(False, lex.is_definition_exists(word))


class TestDefinitionRetrieverFromDict(unittest.TestCase):

    def test_retrieve_definition(self):
        lex = DefinitionRetrieverFromDict()
        word = "module"
        # print(lex.retrieve_definition("module"))
        self.assertEqual(
            ['one of the inherent cognitive or perceptual powers of the mind', 'detachable compartment of a spacecraft',
             'computer circuit consisting of an assembly of electronic components (as of computer hardware)',
             'a self-contained component (unit or item) that is used in combination with other components'],
            lex.retrieve_definition(word))

    # def test_is_definition_exists(self):
    #     lex = DefinitionRetrieverFromDict()
    #     word = "module"
    #     # print(lex.retrieve_definition("module"))
    #     self.assertEqual(True, lex.is_definition_exists(word))
    #
    # def test_is_definition_exists_2(self):
    #     lex = DefinitionRetrieverFromDict()
    #     word = "module4453"
    #     # print(lex.retrieve_definition("module"))
    #     self.assertEqual(False, lex.is_definition_exists(word))
