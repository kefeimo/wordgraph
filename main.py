from __future__ import annotations
from typing import Dict, List, FrozenSet
from wordtree.treefactory import WordTreeFactory
from utils.dataloader import word_definition_dict


if __name__ == "__main__":

    word = "tree"
    tree = WordTreeFactory.create_fullgrowntree(word)
    print("tree.seed", tree.seed)
    print("tree.depth", tree.depth)
    print("number of nodes", len(tree.nodes))
    tree_list = tree.adjacency_list
    print("number of edges", len(tree_list))

    print()
    print("Dependencies at first 2 depths")
    print(tree.nodes_snapshots[:2])
    print("tree definition")
    print(word_definition_dict.get(word))






