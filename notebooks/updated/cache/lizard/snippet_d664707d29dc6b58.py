def train(cls, data, lambda_=1.0):
    first = data.first()
    if not isinstance(first, LabeledPoint):
        raise ValueError('`data` should be an RDD of LabeledPoint')
    labels, pi, theta = callMLlibFunc('trainNaiveBayesModel', data, lambda_)
    return NaiveBayesModel(labels.toArray(), pi.toArray(), numpy.array(theta))