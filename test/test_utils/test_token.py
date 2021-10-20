import unittest
from utils.token import TokenizerV1
from utils.definition import DefinitionRetrieverFromWN


class TestTokenizerV1(unittest.TestCase):

    def test_calc_tokens(self):
        tokenizer = TokenizerV1()
        lex = DefinitionRetrieverFromWN()  # dub
        text = ",".join(lex.retrieve_definition("module"))
        # print(tokenizer.calc_tokens(text))
        self.assertEqual(
            ['one', 'of', 'the', 'inherent', 'cognitive', 'or', 'perceptual', 'powers', 'of', 'the', 'mind', ',',
             'detachable', 'compartment', 'of', 'a', 'spacecraft', ',', 'computer', 'circuit', 'consisting', 'of', 'an',
             'assembly', 'of', 'electronic', 'components', '(', 'as', 'of', 'computer', 'hardware', ')', ',', 'a',
             'self-contained', 'component', '(', 'unit', 'or', 'item', ')', 'that', 'is', 'used', 'in', 'combination',
             'with', 'other', 'components'],
            tokenizer.calc_tokens(text))

    # def test_calc_tokens_w_lexicon(self):
    #     tokenizer = TokenizerV1()
    #     lex = DefinitionRetrieverFromWN()  # dub
    #     text = ",".join(lex.retrieve_definition("module"))
    #     # print(tokenizer.calc_tokens_w_lexicon(text, lex))
    #     self.assertEqual(
    #         ['one', 'inherent', 'cognitive', 'or', 'perceptual', 'powers', 'mind', 'detachable', 'compartment', 'a',
    #          'spacecraft', 'computer', 'circuit', 'consisting', 'an', 'assembly', 'electronic', 'components', 'as',
    #          'computer', 'hardware', 'a', 'self-contained', 'component', 'unit', 'or', 'item', 'is', 'used', 'in',
    #          'combination', 'other', 'components'],
    #         tokenizer.calc_tokens_w_lexicon(text, lex))
