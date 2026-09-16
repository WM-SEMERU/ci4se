def evaluate(self, dataset, metric='auto', missing_value_action='auto'):
    _raise_error_evaluation_metric_is_valid(metric, ['auto', 'accuracy',
        'confusion_matrix', 'roc_curve', 'auc', 'log_loss', 'precision',
        'recall', 'f1_score'])
    return super(_Classifier, self).evaluate(dataset, missing_value_action=
        missing_value_action, metric=metric)