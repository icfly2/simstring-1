import math
from .base import BaseMeasure
from typing import List

class JaccardMeasure(BaseMeasure):
    def min_feature_size(self, query_size: int, alpha: float) -> int:
        return math.ceil(alpha * query_size)

    def max_feature_size(self, query_size: int, alpha: float)-> int:
        return math.floor(query_size / alpha)

    def minimum_common_feature_count(self, query_size: int, y_size: int, alpha: float) -> int:
        return math.ceil(alpha * (query_size + y_size) / (1 + alpha))

    def similarity(self, X: List[int], Y: List[int]) -> float:
        return len(set(X) & set(Y)) / len(set(X) | set(Y))
