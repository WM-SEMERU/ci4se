def set_class_labels(self, class_labels, predicted_feature_name=
    'classLabel', prediction_blob=''):
    spec = self.spec
    nn_spec = self.nn_spec
    if len(spec.description.output) == 0:
        raise ValueError(
            'Model should have at least one output (the probabilities) to automatically make it a classifier.'
            )
    probOutput = spec.description.output[0]
    probOutput.type.dictionaryType.MergeFromString(b'')
    if len(class_labels) == 0:
        return
    class_type = type(class_labels[0])
    if class_type not in [int, str]:
        raise TypeError(
            'Class labels must be of type Integer or String. (not %s)' %
            class_type)
    spec.description.predictedProbabilitiesName = probOutput.name
    spec.description.predictedFeatureName = predicted_feature_name
    classLabel = spec.description.output.add()
    classLabel.name = predicted_feature_name
    if class_type == int:
        nn_spec.ClearField('int64ClassLabels')
        probOutput.type.dictionaryType.int64KeyType.MergeFromString(b'')
        classLabel.type.int64Type.MergeFromString(b'')
        for c in class_labels:
            nn_spec.int64ClassLabels.vector.append(c)
    else:
        nn_spec.ClearField('stringClassLabels')
        probOutput.type.dictionaryType.stringKeyType.MergeFromString(b'')
        classLabel.type.stringType.MergeFromString(b'')
        for c in class_labels:
            nn_spec.stringClassLabels.vector.append(c)
    if prediction_blob != '':
        nn_spec.labelProbabilityLayerName = prediction_blob
    else:
        nn_spec.labelProbabilityLayerName = nn_spec.layers[-1].output[0]