"""
09/29/2021
init,
IDefinitionRetriever, DefinitionRetrieverFromWN,
"""

from __future__ import annotations
from typing import Optional, List, Set, Dict, Union, FrozenSet, Tuple, Iterable
import abc
from nltk.corpus import wordnet
from nltk.corpus.reader.wordnet import Synset
from nltk.stem import WordNetLemmatizer

# import pickle
# from dataclasses import dataclass, field
# import os

from utils.dataloader import word_definition_dict     # data source


class IDefinitionRetriever:
    """
    Interface
    """
    @classmethod
    @abc.abstractmethod
    def retrieve_definition(cls, word: str, *args, **kwargs) -> List[str]:    # to-do use alias for Lexicons: List[str]
        pass

    # @classmethod
    # @abc.abstractmethod
    # def is_definition_exists(cls, word: str, *args, **kwargs) -> bool:
    #     pass


class DefinitionRetrieverFromWN(IDefinitionRetriever):   # to-do: refactor to singleton class using class method
    """
    Concrete class: retrieve lexicons from worldNet API
    """

    @classmethod
    def retrieve_definition(cls, word: str, *args, **kwargs) -> List[str]:
        if not isinstance(word, str):
            print(f"Input: {word}. Type: {type(word)}.")
            raise TypeError("Word requires str Type.")

        definitions: List[str]
        syns: List[Synset] = wordnet.synsets(word)
        if syns:
            definitions = [syn.definition() for syn in syns]
        else:
            definitions = []

        return definitions

    # @classmethod
    # def is_definition_exists(cls, word: str, *args, **kwargs) -> bool:
    #     if cls.retrieve_definition(word):
    #         return True
    #     else:
    #         return False


# @dataclass(frozen=False)    # to-do: refactor to a pure dataclass and preload
# class word_dependency_dict:
#     word_definition_dict: Dict[str, List[str]] = field(init=False, repr=False)
#
#     @classmethod
#     def __post_init__(cls):
#         this_dir, this_filename = os.path.split(__file__)
#         data_path = os.path.join(this_dir, './data/word_definition_dict.pickle')
#         with open(data_path, 'rb') as f:
#             cls.wordnet_dict: Dict[str, FrozenSet[str]] = pickle.load(f)


class DefinitionRetrieverFromDict(IDefinitionRetriever):
    """
    Concrete class: retrieve definitions from an extracted dictionary
    note: the keys of the dict are in lowercase
    """
    _word_dependencies_dict: Dict[str, FrozenSet[str]] = word_definition_dict

    @classmethod
    def retrieve_definition(cls, word: str, *args, **kwargs) -> List[str]:
        if not isinstance(word, str):
            print(f"Input: {word}. Type: {type(word)}.")
            raise TypeError("Word requires str Type.")

        definitions: List[str]
        result: Optional[List[str]] = cls._word_dependencies_dict.get(word)
        if result:
            definitions = result
        else:
            definitions = []

        return definitions


class DefinitionRetrieverFromDictV2(IDefinitionRetriever):
    """
    Concrete class: retrieve definitions from an extracted dictionary
    note: the keys of the dict are in lowercase
    V2: perform lemmatization in pre- and post- processing
    """
    _word_definition_dict: Dict[
        str, FrozenSet[str]] = word_definition_dict

    @classmethod
    def retrieve_definition(cls, word: str, *args, **kwargs) -> List[str]:
        if not isinstance(word, str):
            print(f"Input: {word}. Type: {type(word)}.")
            raise TypeError("Word requires str Type.")

        definitions: List[str]
        result: Optional[List[str]] = cls._word_definition_dict.get(word)
        if result:
            definitions = result
        else:
            word_lemma = WordNetLemmatizer().lemmatize(word)    # retry with the new word (wordy but better performance)
            result_lemma: Optional[List[str]] = cls._word_definition_dict.get(word_lemma)
            if result_lemma:
                definitions = result_lemma
            else:
                definitions = []

        return definitions




