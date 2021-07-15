from .cosine import CosineMeasure
from .dice import DiceMeasure
from .jaccard import JaccardMeasure

from typing import Union

Measure = Union[CosineMeasure, DiceMeasure, JaccardMeasure]
