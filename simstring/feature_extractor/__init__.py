from .character_ngram import CharacterNgramFeatureExtractor
from .word_ngram import WordNgramFeatureExtractor
from typing import Union

try:
    from .mecab_ngram import MecabNgramFeatureExtractor
    FeatureExtractor = Union[CharacterNgramFeatureExtractor, MecabNgramFeatureExtractor, WordNgramFeatureExtractor]
except ImportError:
    FeatureExtractor = Union[CharacterNgramFeatureExtractor, WordNgramFeatureExtractor]
