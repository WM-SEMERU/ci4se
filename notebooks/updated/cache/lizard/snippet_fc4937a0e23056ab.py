def _check_classifier(classifier):
    predict = getattr(classifier, 'predict', None)
    if not callable(predict):
        raise ValueError('Classifier does not have predict method!')
    predict_proba = getattr(classifier, 'predict_proba', None)
    if not callable(predict_proba):
        raise ValueError('Classifier does not have predict_proba method!')