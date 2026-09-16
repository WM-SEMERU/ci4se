def get_rec_features(self, features=None):
    if features is None:
        features = self.dist_funcs.keys()
    elif not isinstance(features, list):
        features = [features]
    return self.rec.applymap(lambda x: {k: v for k, v in x.items() if k !=
        'item'} if x is not None else None)