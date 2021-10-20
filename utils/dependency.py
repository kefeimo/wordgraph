"""
10/06/2021
refactor to centralized data source loading
"""

from __future__ import annotations
from typing import Optional, List, Set, Dict, Union, FrozenSet, Tuple, Iterable, Callable
import abc
from utils.definition import *
from utils.token import *
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import functools


from utils.dataloader import word_dependency_dict, word_dependency_dict_ext     # data source


class IDependencySelector:

    @abc.abstractmethod
    def calc_dependencies(self, word: str, *args, **kwargs) -> FrozenSet[str]:  # to-do: alias dependencies
        pass


class DependencySelectorTemplate(IDependencySelector):
    """
    A template class for code reuse
    """
    # definition_retriever: IDefinitionRetriever
    _retrieve_definition_func: Callable[..., List[str]]
    # tokenizer: ITokenizer
    _calc_token_func: Callable[..., List[str]]

    @classmethod
    def calc_dependencies(cls, word: str, *args, **kwargs) -> FrozenSet[str]:
        if not isinstance(word, str):
            raise TypeError("`word` requires `str` Type")
        return cls._calc_dependencies_helper(word)

    @classmethod
    def _calc_dependencies_helper(cls, word: str, *args, **kwargs) -> FrozenSet[str]:

        definitions = cls._retrieve_definition_func(word)
        if definitions:
            definition_str = " ".join(definitions)
            tokens_list = cls._calc_token_func(definition_str)
            dependencies: FrozenSet[str] = frozenset(
                [token.lower() for token in set(tokens_list)])  # use lower() for post-proc
        else:
            dependencies = frozenset()

        return dependencies


class LegalDependencySelectorTemplate(DependencySelectorTemplate):
    """
    A template class for code reuse
    """

    @classmethod
    def calc_dependencies(cls, word: str, *args, **kwargs) -> FrozenSet[str]:
        """
        legal dependencies are words with definitions in the reference dictionary
        """
        if not isinstance(word, str):
            raise TypeError("`word` requires `str` Type")
        raw_dependencies = cls._calc_dependencies_helper(word)
        legal_dependencies: FrozenSet[str] = frozenset([word for word in raw_dependencies
                                                        if cls._retrieve_definition_func(word)])
        return legal_dependencies


class RawDependencySelectorFromDict(DependencySelectorTemplate):
    _retrieve_definition_func: Callable[..., List[str]] = DefinitionRetrieverFromDict.retrieve_definition
    _calc_token_func: Callable[..., List[str]] = TokenizerV1.calc_tokens


class RawDependencySelectorFromWN(DependencySelectorTemplate):
    _retrieve_definition_func: Callable[..., List[str]] = DefinitionRetrieverFromWN.retrieve_definition
    _calc_token_func: Callable[..., List[str]] = TokenizerV1.calc_tokens


class LegalDependencySelectorFromDict(LegalDependencySelectorTemplate):
    _retrieve_definition_func: Callable[..., List[str]] = DefinitionRetrieverFromDict.retrieve_definition
    _calc_token_func: Callable[..., List[str]] = TokenizerV1.calc_tokens


class LegalDependencySelectorFromWN(LegalDependencySelectorTemplate):
    _retrieve_definition_func: Callable[..., List[str]] = DefinitionRetrieverFromWN.retrieve_definition
    _calc_token_func: Callable[..., List[str]] = TokenizerV1.calc_tokens


# @dataclass(frozen=False)  # to-do: refactor to a pure dataclass and preload
# class word_dependency_dict:
#     word_dependency_dict: Dict[str, List[str]] = field(init=False, repr=False)
#     word_dependency_dict_ext: Dict[str, List[str]] = field(init=False, repr=False)
#
#     @classmethod
#     def __post_init__(cls):
#         this_dir, this_filename = os.path.split(__file__)
#         data_path = os.path.join(this_dir, './data/word_dep_dict.pickle')
#         with open(data_path, 'rb') as f:
#             cls.word_dependency_dict: Dict[str, FrozenSet[str]] = pickle.load(f)
#         data_path_2 = os.path.join(this_dir, './data/word_dep_dict_ext.pickle')
#         with open(data_path_2, 'rb') as f:
#             cls.word_dependency_dict_ext: Dict[str, FrozenSet[str]] = pickle.load(f)


class RawDependencySelectorFastV2(IDependencySelector):
    """
    Utilize a pre-extracted dict
    note: the keys of the dict are in lowercase
    V2: perform lemmatization in pre- and post- processing (aggressive search)
    """
    _word_dependency_dict: Dict[str, FrozenSet[str]] = word_dependency_dict

    @classmethod
    def calc_dependencies(cls, word: str, *args, **kwargs) -> FrozenSet[str]:
        dependencies: FrozenSet[str]
        if cls._word_dependency_dict.get(word):
            dependencies = cls._word_dependency_dict.get(word)
        else:
            word_lemma = WordNetLemmatizer().lemmatize(word)  # retry with the new word (wordy but better performance)
            result_lemma: Optional[FrozenSet[str]] = cls._word_dependency_dict.get(word_lemma)
            if result_lemma:
                dependencies = result_lemma
            else:
                dependencies = frozenset()
        return dependencies


class LegalDependencySelectorFastV2(IDependencySelector):
    """
    Utilize a pre-extracted dict
    note: the keys of the dict are in lowercase
    V2: perform lemmatization in pre- and post- processing (aggressive search)
    """
    _word_dependency_dict: Dict[str, FrozenSet[str]] = word_dependency_dict_ext

    @classmethod
    def calc_dependencies(cls, word: str, *args, **kwargs) -> FrozenSet[str]:
        legal_dependencies_lemma: FrozenSet[str]
        raw_dependencies = cls._word_dependency_dict.get(word)
        if raw_dependencies:
            legal_dependencies_lemma = cls._lemma_helper(raw_dependencies)
        else:
            word_lemma = WordNetLemmatizer().lemmatize(word)  # retry with the new word (wordy but better performance)
            raw_dependencies_lemma: Optional[FrozenSet[str]] = cls._word_dependency_dict.get(word_lemma)
            if raw_dependencies_lemma:
                legal_dependencies_lemma = cls._lemma_helper(raw_dependencies_lemma)
            else:
                legal_dependencies_lemma = frozenset()
        return legal_dependencies_lemma

    @classmethod
    def _lemma_helper(cls, dependency_candidates: FrozenSet[str]) -> FrozenSet[str]:
        # return a frozenset of legal, lemmatized dependencies
        return frozenset([WordNetLemmatizer().lemmatize(word) for word in dependency_candidates
                          if cls._word_dependency_dict.get(WordNetLemmatizer().lemmatize(word))])


# default
class RawDependencySelectorFast(IDependencySelector):
    """
    Utilize a pre-extracted dict
    note: the keys of the dict are in lowercase
    """
    _word_dependency_dict: Dict[str, FrozenSet[str]] = word_dependency_dict_ext

    @classmethod
    def calc_dependencies(cls, word: str, *args, **kwargs) -> FrozenSet[str]:
        dependencies: FrozenSet[str]
        word = word.lower()
        if cls._word_dependency_dict.get(word):
            dependencies = cls._word_dependency_dict.get(word)
        else:
            dependencies = frozenset()
        return dependencies


# default
class LegalDependencySelectorFast(IDependencySelector):
    """
    Utilize a pre-extracted dict and WordNet lemmatizer for processing
    note: the keys of the dict are in lowercase
    """
    _word_dependency_dict: Dict[str, FrozenSet[str]] = word_dependency_dict_ext

    @classmethod
    def calc_dependencies(cls, word: str, *args, **kwargs) -> FrozenSet[str]:

        legal_dependencies: FrozenSet[str]
        word = word.lower()
        raw_dependencies = cls._word_dependency_dict.get(word)
        if raw_dependencies:
            legal_dependencies = frozenset([word for word in raw_dependencies
                                            if cls._word_dependency_dict.get(word)])
        else:
            legal_dependencies = frozenset()
        return legal_dependencies


# ----------------------------------

class IDependencySpanner:

    @abc.abstractmethod
    def span_dependencies(self, word: str, *args, **kwargs) -> ...:  # to-do: use alias ...
        pass


class DependencySpannerTemplate(IDependencySpanner):
    # dependency_selector: IDependencySelector
    _calc_dependency_func: Callable[..., FrozenSet[str]]  # calc_dependencies


    @classmethod
    def span_dependencies(cls, seed: str, depth_max: int = 3, *args, **kwargs) -> Tuple[Set[str],
                                                                                        List[Set[str]],
                                                                                        List[Set[str]]]:
        # input validation
        if not isinstance(seed, str):
            raise TypeError("`word` requires `str` Type")
        if not isinstance(depth_max, int):
            raise TypeError("`depth_max` requires `int` Type")
        seeds_all, seeds_nextrnd_records = cls._span_dependencies_inner({seed}, {seed}, [], 0,
                                                                        iteration_limit=depth_max)
        nodes_snapshots = cls._get_nodes_snapshots(seed, seeds_nextrnd_records)
        return seeds_all, seeds_nextrnd_records, nodes_snapshots

    @classmethod
    def _span_dependencies_inner(cls, seeds: Set[str], seeds_all: Set[str], seeds_nextrnd_records: List[Set[str]],
                                 count: int, iteration_limit: int) -> Tuple[Set[str], List[Set[str]]]:
        """

        """
        # map-reduce: get unseen dependencies of seeds
        dependencies_unseen_per_seed: Iterable[Set[str]] = map(
            lambda seed, seeds_all_inner: cls._get_unseen_dependencies(seed, seeds_all_inner),
            seeds, len(seeds) * [seeds_all])
        seeds_nextrnd: Set[str] = functools.reduce(lambda x, y: x.union(y), dependencies_unseen_per_seed, set())
        # update states
        if seeds_nextrnd:  # not empty
            seeds_all.update(seeds_nextrnd.copy())  # python gotcha late binding
            seeds_nextrnd_records.append(seeds_nextrnd.copy())  # python gotcha late binding
        count += 1
        # check stop criteria
        if iteration_limit == 0:
            return seeds, list()
        elif seeds_nextrnd and count < iteration_limit:
            return cls._span_dependencies_inner(seeds_nextrnd, seeds_all, seeds_nextrnd_records,
                                                count, iteration_limit)
        else:
            return seeds_all, seeds_nextrnd_records

    # @staticmethod
    @classmethod
    def _get_unseen_dependencies(cls, word: str, words_seen: Set[str]) -> Set[str]:
        if not isinstance(word, str):
            raise TypeError("`word` requires `str` Type")

        new_dependencies: Set[str]
        dependencies_raw: FrozenSet[str] = cls._calc_dependency_func(word)
        if dependencies_raw:
            new_dependencies = set([dep for dep in dependencies_raw if
                                    dep and dep not in words_seen])
        else:
            new_dependencies = set()
        return new_dependencies

    # @staticmethod
    @classmethod
    def _get_nodes_snapshots(cls, seed: str, seeds_nextrnd_records: List[Set[str]]) -> List[Set[str]]:
        """
        get a list of accumulated nodes snapshots from _seeds_nextrnd_records
        """
        nodes_tilnow: Set[str] = {seed}
        nodes_records: List[Set[str]] = [{seed}]
        for nextrnd_seeds in seeds_nextrnd_records:
            if nextrnd_seeds:  # not empty
                nodes_tilnow.update(nextrnd_seeds)
                nodes_records.append(nodes_tilnow.copy())
        return nodes_records  # do not take the first one to make the same length as len(seeds_nextrnd_records)


# default
class RawDependencySpannerFast(DependencySpannerTemplate):
    _calc_dependency_func: Callable[..., FrozenSet[str]] = RawDependencySelectorFast.calc_dependencies


# default
class LegalDependencySpannerFast(DependencySpannerTemplate):
    _calc_dependency_func: Callable[..., FrozenSet[str]] = LegalDependencySelectorFast.calc_dependencies


class RawDependencySpannerFastV2(DependencySpannerTemplate):
    _calc_dependency_func: Callable[..., FrozenSet[str]] = RawDependencySelectorFastV2.calc_dependencies


class LegalDependencySpannerFastV2(DependencySpannerTemplate):
    _calc_dependency_func: Callable[..., FrozenSet[str]] = LegalDependencySelectorFastV2.calc_dependencies


class RawDependencySpannerFromDict(DependencySpannerTemplate):
    _calc_dependency_func: Callable[..., FrozenSet[str]] = RawDependencySelectorFromDict.calc_dependencies


class RawDependencySpannerFromWN(DependencySpannerTemplate):
    _calc_dependency_func: Callable[..., FrozenSet[str]] = RawDependencySelectorFromWN.calc_dependencies


class LegalDependencySpannerFromDict(DependencySpannerTemplate):
    _calc_dependency_func: Callable[..., FrozenSet[str]] = LegalDependencySelectorFromDict.calc_dependencies


class LegalDependencySpannerFromWN(DependencySpannerTemplate):
    _calc_dependency_func: Callable[..., FrozenSet[str]] = LegalDependencySelectorFromWN.calc_dependencies
