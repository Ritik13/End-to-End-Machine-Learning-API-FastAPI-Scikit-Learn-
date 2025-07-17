import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin

class NumericFeatureTransformer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        review_length = X.apply(len)
        word_count = X.apply(lambda x: len(x.split()))
        repeated_ratio = X.apply(
            lambda x: 1 - (len(set(x.lower().split())) / len(x.split())) if len(x.split()) > 0 else 0
        )
        return np.c_[review_length, word_count, repeated_ratio]
