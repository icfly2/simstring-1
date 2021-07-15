from collections import defaultdict
from .base import BaseDatabase
from typing import List
from simstring.feature_extractor import FeatureExtractor

def defaultdict_set() -> defaultdict:
    return defaultdict(set)

class DictDatabase(BaseDatabase):
    def __init__(self, feature_extractor: FeatureExtractor)  -> None:
        self.feature_extractor = feature_extractor
        self.strings = []
        self.feature_set_size_to_string_map = defaultdict(set)
        self.feature_set_size_and_feature_to_string_map = defaultdict(defaultdict_set)

    def add(self, string: str) -> None:
        features = self.feature_extractor.features(string)
        size = len(features)
        self.strings.append(string)
        self.feature_set_size_to_string_map[size].add(string)
        for feature in features:
            self.feature_set_size_and_feature_to_string_map[size][feature].add(string)

    def all(self) -> List[str]:
        return self.strings

    def lookup_strings_by_feature_set_size_and_feature(self, size: int, feature: str) -> set:
        return self.feature_set_size_and_feature_to_string_map[size][feature]

    def min_feature_size(self) -> int:
        return min(self.feature_set_size_to_string_map.keys())

    def max_feature_size(self)  -> int:
        return max(self.feature_set_size_to_string_map.keys())
