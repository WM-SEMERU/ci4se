def discretize(self, data):
    ret = data.copy()
    for feature in self.lambdas:
        if len(data.shape) == 1:
            ret[feature] = int(self.lambdas[feature](ret[feature]))
        else:
            ret[:, (feature)] = self.lambdas[feature](ret[:, (feature)]
                ).astype(int)
    return ret