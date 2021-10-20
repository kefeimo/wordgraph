from __future__ import annotations
from typing import Dict, List, FrozenSet

from utils.dataloader import WordnetDict

if __name__ == "__main__":

    dict_test: Dict[str, FrozenSet[str]] = WordnetDict
    print(len(dict_test.keys()))

    item_test= [i for i in dict_test.items()][0]
    print(type(item_test[1]))




