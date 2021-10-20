from __future__ import annotations
from typing import Optional, List, Set, Dict, Union, TypedDict, Tuple, FrozenSet
import abc
from utils import dependency
from dataclasses import dataclass, field
import attr
from functools import lru_cache
from itertools import accumulate
from wordtree.tree import *


class ITreeFactory:

    @staticmethod
    @abc.abstractmethod
    def create_tree(seed: str, *args, **kwargs):
        pass


class WordTreeFactory(ITreeFactory):

    @staticmethod
    def create_tree(seed: str, depth: int = 0, *args, **kwargs) -> WordTree:
        wordtree: WordTree = WordTreeFactory._create_wordtree_cache(seed)
        wordtree.modify_depth(depth)
        return wordtree

    @staticmethod
    @lru_cache  # only one instance with the same _seed value - a relaxed singleton
    def _create_wordtree_cache(seed: str) -> WordTree:
        return WordTree(seed)

    @staticmethod
    @lru_cache
    def create_fullgrowntree(seed: str) -> WordTreeFullGrown:
        wordtree: WordTree = WordTree(seed)
        wordtree.modify_depth(100)  # magic number 100 to make sure hit the maximum depth
        adjacent_list = wordtree.to_adjacentlist()

        return WordTreeFullGrown(seed=wordtree.seed,
                                 depth=wordtree.depth,
                                 nodes=wordtree.nodes,
                                 seeds_nextrnd_records=wordtree.nodes_snapshots,
                                 nodes_snapshots=wordtree.nodes_snapshots,
                                 adjacent_list=adjacent_list)
