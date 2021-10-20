

from __future__ import annotations
from typing import Optional, List, Set, Dict, Union, FrozenSet, Tuple, Iterable
import abc
from utils.definition import IDefinitionRetriever
from nltk.tokenize import word_tokenize


class ITokenizer:

    @classmethod
    @abc.abstractmethod
    def calc_tokens(cls, text: str, *args, **kwargs) -> List[str]:  # to-do: use alias tokens: List[str]
        pass


class TokenizerV1(ITokenizer):
    """
    Perform tokenization with pre- or post- processing
    processing: lower, (no need to make unique, or only-alpha at this point)
    """

    @classmethod
    def calc_tokens(cls, text: str, *args, **kwargs) -> List[str]:
        tokens: List[str]
        if not isinstance(text, str):
            raise TypeError("`text` requires `str` Type")

        text_lower = text.lower()
        tokens = word_tokenize(text_lower)

        return tokens


class TokenizerV2(ITokenizer):  # to-do: write your own tokenizer
    pass

