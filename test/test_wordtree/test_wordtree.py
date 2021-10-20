"""
09/21/2021 v0.1 init

"""

import unittest
from wordtree.tree import *
from wordtree.treefactory import *
import dataclasses


class TestWordTree(unittest.TestCase):

    # test _create_wordtree_cache
    def test_create_wordtree(self):
        wordtree_test: WordTree = WordTreeFactory._create_wordtree_cache("seed")
        self.assertEqual("seed", wordtree_test.seed)
        self.assertEqual(0, wordtree_test.depth)
        self.assertEqual({'seed'}, wordtree_test.nodes)

    # test caching
    def test_caching(self):
        wordtree_test_1: WordTree = WordTreeFactory._create_wordtree_cache("seed")
        wordtree_test_2: WordTree = WordTreeFactory._create_wordtree_cache("seed")
        wordtree_test_3: WordTree = WordTreeFactory._create_wordtree_cache("seed")
        wordtree_test_4: WordTree = WordTreeFactory._create_wordtree_cache("seed2")
        self.assertEqual(True, wordtree_test_1 is wordtree_test_2 is wordtree_test_3)
        self.assertEqual(False, wordtree_test_1 is wordtree_test_2 is wordtree_test_4)

    # test modify_depth
    def test_modify_depth(self):
        wordtree_test: WordTree = WordTreeFactory._create_wordtree_cache("seed")
        wordtree_test.modify_depth(1)
        self.assertEqual(1, wordtree_test.depth)
        wordtree_test.modify_depth(4)
        self.assertEqual(4, wordtree_test.depth)
        wordtree_test.modify_depth(10)
        self.assertEqual(10, wordtree_test.depth)
        wordtree_test.modify_depth(6)
        self.assertEqual(6, wordtree_test.depth)
        wordtree_test.modify_depth(0)
        self.assertEqual(0, wordtree_test.depth)

    # test modify_depth error handling depth_aim >=0
    def test_modify_depth_2(self):
        wordtree_test: WordTree = WordTreeFactory._create_wordtree_cache("seed")
        with self.assertRaises(ValueError):
            wordtree_test.modify_depth(-9)

    # test modify_depth back to zero
    def test_modify_depth_3(self):
        wordtree_test: WordTree = WordTreeFactory._create_wordtree_cache("seed")
        wordtree_test.modify_depth(10)
        wordtree_test.modify_depth(0)
        self.assertEqual("seed", wordtree_test.seed)
        self.assertEqual(0, wordtree_test.depth)
        self.assertEqual({'seed'}, wordtree_test.nodes)

    # test depth limit
    def test_depth_limit(self):
        wordtree_test: WordTree = WordTreeFactory._create_wordtree_cache("seed")
        wordtree_test.modify_depth(30)
        self.assertEqual(15, wordtree_test.depth)
        self.assertEqual(15, wordtree_test.depth_limit)

    # test get_nodes_snapshots
    def test_get_nodes_snapshots(self):
        wordtree_test: WordTree = WordTreeFactory._create_wordtree_cache("seed")
        wordtree_test.modify_depth(1)
        # print(wordtree_test.nodes)
        # print(wordtree_test.nodes_snapshots)
        # print(wordtree_test._WordTree__seeds_nextrnd_records)
        self.assertEqual("seed", wordtree_test.seed)
        self.assertEqual(1, wordtree_test.depth)
        self.assertEqual([{'seed'},
                          {'a', 'an', 'bear', 'by', 'cause', 'coat', 'consisting', 'containing', 'development',
                           'disperse', 'distribute', 'early', 'ejaculated', 'embryo', 'enterprise', 'fertilized',
                           'fluid', 'food', 'fruit', 'future', 'genital', 'go', 'ground', 'growth', 'hard', 'having',
                           'help', 'in', 'inoculate', 'inspiration', 'iodide', 'is', 'its', 'later', 'male', 'mature',
                           'meet', 'microorganisms', 'money', 'not', 'on', 'one', 'or', 'outstanding', 'ovule',
                           'particles', 'place', 'plant', 'players', 'protective', 'provides', 'providing', 'rain',
                           'remove', 'rounds', 'seed', 'seeds', 'shed', 'silver', 'small', 'so', 'source',
                           'spermatozoa', 'sprinkle', 'stages', 'teams', 'testa', 'thick', 'tournament', 'tract',
                           'white', 'will', 'work'}], wordtree_test.nodes_snapshots)

    # test to_adjacentlist
    def test_to_adjacentlist(self):
        wordtree_test: WordTree = WordTreeFactory._create_wordtree_cache("seed")
        wordtree_test.modify_depth(0)
        adlist = wordtree_test.to_adjacentlist()
        self.assertEqual({'seed': frozenset(
            {'a', 'an', 'bear', 'by', 'cause', 'coat', 'consisting', 'containing', 'development', 'disperse',
             'distribute', 'early', 'ejaculated', 'embryo', 'enterprise', 'fertilized', 'fluid', 'food', 'fruit',
             'future', 'genital', 'go', 'ground', 'growth', 'hard', 'having', 'help', 'in', 'inoculate', 'inspiration',
             'iodide', 'is', 'its', 'later', 'male', 'mature', 'meet', 'microorganisms', 'money', 'not', 'on', 'one',
             'or', 'outstanding', 'ovule', 'particles', 'place', 'plant', 'players', 'protective', 'provides',
             'providing', 'rain', 'remove', 'rounds', 'seed', 'seeds', 'shed', 'silver', 'small', 'so', 'source',
             'spermatozoa', 'sprinkle', 'stages', 'teams', 'testa', 'thick', 'tournament', 'tract', 'white', 'will',
             'work'})},
            adlist)

    # test attribute error handling set not allowed
    def test_attribute_error_handling(self):
        wordtree_test: WordTree = WordTreeFactory._create_wordtree_cache("seed")
        with self.assertRaisesRegex(AttributeError, "can't set attribute"):
            wordtree_test.seed = "new seed"
        self.assertEqual("seed", wordtree_test.seed)


class TestWordTreeFullGrown(unittest.TestCase):

    # test _create_wordtree_cache
    def test_create_wordtree(self):
        wordtree_fullgrown_test: WordTreeFullGrown = WordTreeFactory.create_fullgrowntree("seed")
        wordtree_test: WordTree = WordTreeFactory._create_wordtree_cache("seed")
        wordtree_test.modify_depth(30)
        self.assertEqual("seed", wordtree_fullgrown_test.seed)
        self.assertEqual(wordtree_test.depth, wordtree_fullgrown_test.depth)
        self.assertEqual(wordtree_test.nodes, wordtree_fullgrown_test.nodes)

    # test caching
    def test_caching(self):
        wordtree_test_1: WordTreeFullGrown = WordTreeFactory.create_fullgrowntree("seed")
        wordtree_test_2: WordTreeFullGrown = WordTreeFactory.create_fullgrowntree("seed")
        wordtree_test_3: WordTreeFullGrown = WordTreeFactory.create_fullgrowntree("seed")
        wordtree_test_4: WordTree = WordTreeFactory._create_wordtree_cache("seed")
        wordtree_test_5: WordTreeFullGrown = WordTreeFactory.create_fullgrowntree("seed2")
        self.assertEqual(True, wordtree_test_1 is wordtree_test_2 is wordtree_test_3)
        self.assertEqual(False, wordtree_test_1 is wordtree_test_2 is wordtree_test_4)
        self.assertEqual(False, wordtree_test_1 is wordtree_test_2 is wordtree_test_5)

    # test modify_depth (pass not modifiable. immutable class)
    def test_modify_depth(self):
        pass

    # test depth limit
    def test_depth_limit(self):
        wordtree_test: WordTreeFullGrown = WordTreeFactory.create_fullgrowntree("seed")
        self.assertEqual(15, wordtree_test.depth)

    # test get_nodes_snapshots
    def test_get_nodes_snapshots(self):
        wordtree_fullgrown_test: WordTreeFullGrown = WordTreeFactory.create_fullgrowntree("seed")
        wordtree_test: WordTree = WordTreeFactory._create_wordtree_cache("seed")
        wordtree_test.modify_depth(30)
        self.assertEqual(wordtree_test.nodes_snapshots, wordtree_fullgrown_test.nodes_snapshots)

    # test to_adjacentlist
    def test_to_adjacentlist(self):
        wordtree_fullgrown_test: WordTreeFullGrown = WordTreeFactory.create_fullgrowntree("seed")
        wordtree_test: WordTree = WordTreeFactory._create_wordtree_cache("seed")
        wordtree_test.modify_depth(30)
        self.assertEqual(wordtree_test.to_adjacentlist(), wordtree_fullgrown_test.adjacent_list)

    # test to_adjacentlist speed
    def test_to_adjacentlist_2(self):
        wordtree_fullgrown_test: WordTreeFullGrown = WordTreeFactory.create_fullgrowntree("seed")
        wordtree_fullgrown_test.adjacent_list
        # wordtree_test: WordTree = WordTreeFactory._create_wordtree_cache("seed")
        # wordtree_test.modify_depth(30)
        # self.assertEqual(wordtree_test.to_adjacentlist(), wordtree_fullgrown_test.adjacent_list)

    # immutable dataclass WordTreeFullGrown, frozen=True, not allow change
    def test_attribute_error_handling(self):
        wordtree_fullgrown_test: WordTreeFullGrown = WordTreeFactory.create_fullgrowntree("seed")
        with self.assertRaises(dataclasses.FrozenInstanceError):
            wordtree_fullgrown_test.seed = "new seed"
        self.assertEqual("seed", wordtree_fullgrown_test.seed)
