def create(dataset, target, features=None, validation_set='auto', verbose=True
    ):
    return _sl.create_classification_with_model_selector(dataset, target,
        model_selector=_turicreate.extensions._supervised_learning.
        _classifier_available_models, features=features, validation_set=
        validation_set, verbose=verbose)