from sklearn.base import BaseEstimator, TransformerMixin

class FeatureEnhancer(BaseEstimator):
    def fit(self, X, y=None):
        return self

    def transform(self, X):      
        
        def get_is_center(district):
            if district is "Wilda":
                return 1
            return 0
        
        out = X.copy()
        out['is_center'] = X['location'].map(get_is_center)
        return out[['sqrMeters', 'rooms','is_center']]