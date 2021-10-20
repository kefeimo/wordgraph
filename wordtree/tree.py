from __future__ import annotations
from typing import Optional, List, Set, Dict, Union, TypedDict, Tuple, FrozenSet, Callable
import abc
from utils.dependency import LegalDependencySpannerFast, LegalDependencySelectorFast
from dataclasses import dataclass, field


@dataclass(frozen=True)
class WordTreeFullGrown:
    seed: str
    depth: int
    nodes: Set[str]
    seeds_nextrnd_records: List[Set[str]]
    nodes_snapshots: List[Set[str]]
    adjacent_list: Dict[str, FrozenSet[str]]

    def __repr__(self):
        return f"{self.__class__.__name__}(seed={self.seed}, depth={self.depth})"


@dataclass  # to-do: the point of using dataclass is to avoid many getset. then why I still have to use property
class WordTreeTemplate:  # to-do: avoid direct instantiation
    _seed: str
    _depth: int
    _nodes: Set[str]
    _seeds_nextrnd_records: List[Set[str]]
    _nodes_snapshots: List[Set[str]]
    _depth_limit: Optional[int]

    _span_dependency_func: Callable
    _calc_dependency_func: Callable

    def __init__(self, seed: str):
        self._seed = seed
        self._depth = 0
        self._nodes, self._seeds_nextrnd_records, self._nodes_snapshots \
            = self._span_dependency_func(self._seed,
                                         self._depth)  # return {seed}, [Set()], [{seed}] if depth=0
        self._depth_limit = None

    @property
    def seed(self):
        return self._seed

    @property
    def depth(self):
        return self._depth

    @property
    def nodes(self):
        return self._nodes

    @property
    def seeds_nextrnd_records(self):
        return self._seeds_nextrnd_records

    @property
    def nodes_snapshots(self):
        return self._nodes_snapshots

    @property
    def depth_limit(self):
        return self._depth_limit

    def __repr__(self):
        return f"{self.__class__.__name__}(seed={self.seed}, depth={self.depth}, depth_limit={self.depth_limit})"

    def modify_depth(self, depth_aim: int) -> None:
        """
        modify depth_aim allows update _nodes, _seeds_nextrnd_records
        note: the actual depth_aim can be different from the set depth_aim. especially when the depth_aim hit the limit
        """
        if depth_aim < 0:
            raise ValueError("`depth_aim` requires >= 0.")

        self._nodes, self._seeds_nextrnd_records, self._nodes_snapshots = \
            self._span_dependency_func(self._seed, depth_aim)
        self._depth = len(self._seeds_nextrnd_records)  # update the actual _depth
        if self._depth < depth_aim:  # update the depth_aim limit
            self._depth_limit = self._depth

    def to_adjacentlist(self) -> Dict[str, FrozenSet[str]]:
        """
        represent topology in adjacent list,
        e.g. {seed1: {depnd1, depend2, ...}, seed2: {depnd10, depnd32, ...}, ...}
        """

        # init
        ajlist: Dict[str, FrozenSet[str]] = dict()
        nodes_list: List[Set[str]] = [{self._seed}] + self._seeds_nextrnd_records
        for seeds in nodes_list:
            if seeds:  # not empty
                for seed in seeds:
                    ajlist.update({seed: self._calc_dependency_func(seed)})
        return ajlist


class WordTree(WordTreeTemplate):
    _span_dependency_func: Callable = LegalDependencySpannerFast.span_dependencies
    _calc_dependency_func: Callable = LegalDependencySelectorFast.calc_dependencies
