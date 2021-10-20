"""
10/06/2021 init
"""

from __future__ import annotations
from typing import Dict, List, FrozenSet, Optional
from importlib import resources     # >= 3.7
import pickle

# import utils.data   # package in importlib.resources


class _WordnetDict:
    _word_dependency_dict: Dict[str, List[str]]
    _word_dependency_dict_ext: Dict[str, List[str]]

    def __init__(self):
        self._word_dependency_dict: Optional[Dict[str, FrozenSet[str]]] = None
        self._word_dependency_dict_ext: Optional[Dict[str, FrozenSet[str]]] = None
        self._word_definition_dict: Optional[Dict[str, List[str]]] = None

    @property
    def word_dependency_dict(self) -> Dict[str, FrozenSet[str]]:     # lazy loading data source
        word_dependency_dict_: Dict[str, FrozenSet[str]]
        if not self._word_dependency_dict:
            with resources.open_binary('utils.data', 'word_dep_dict.pickle') as f:
                word_dependency_dict_ = pickle.load(f)
        else:
            word_dependency_dict_ = self._word_dependency_dict
        return word_dependency_dict_

    @property
    def word_dependency_dict_ext(self) -> Dict[str, FrozenSet[str]]:     # lazy loading data source
        word_dependency_dict_ext_: Dict[str, FrozenSet[str]]
        if not self._word_dependency_dict_ext:
            with resources.open_binary('utils.data', 'word_dep_dict_ext.pickle') as f:
                word_dependency_dict_ext_ = pickle.load(f)
        else:
            word_dependency_dict_ext_ = self._word_dependency_dict_ext
        return word_dependency_dict_ext_

    @property
    def word_definition_dict(self) -> Dict[str, List[str]]:     # lazy loading data source
        word_definition_dict_: Dict[str, List[str]]
        if not self._word_definition_dict:
            with resources.open_binary('utils.data', 'word_definition_dict.pickle') as f:
                word_definition_dict_ = pickle.load(f)
        else:
            word_definition_dict_ = self._word_definition_dict
        return word_definition_dict_


word_dependency_dict: Dict[str, FrozenSet[str]] = _WordnetDict().word_dependency_dict
word_dependency_dict_ext: Dict[str, FrozenSet[str]] = _WordnetDict().word_dependency_dict_ext
word_definition_dict: Dict[str, List[str]] = _WordnetDict().word_definition_dict

