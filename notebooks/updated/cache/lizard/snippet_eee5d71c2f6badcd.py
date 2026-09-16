def replace_nan(trainingset, replace_with=None):
    training_data = np.array([instance.features for instance in trainingset]
        ).astype(np.float64)

    def encoder(dataset):
        for instance in dataset:
            instance.features = instance.features.astype(np.float64)
            if np.sum(np.isnan(instance.features)):
                if replace_with == None:
                    instance.features[np.isnan(instance.features)] = means[
                        np.isnan(instance.features)]
                else:
                    instance.features[np.isnan(instance.features)
                        ] = replace_with
        return dataset
    if replace_nan_with == None:
        means = np.mean(np.nan_to_num(training_data), axis=0)
    return encoder