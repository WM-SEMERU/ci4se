def predict(self, lon, lat, **kwargs):
    assert self.classifier is not None, 'ERROR'
    pred = np.zeros(len(lon))
    cut_geometry, flags_geometry = self.applyGeometry(lon, lat)
    x_test = []
    for key, operation in self.config['operation']['params_intrinsic']:
        assert operation.lower() in ['linear', 'log'], 'ERROR'
        if operation.lower() == 'linear':
            x_test.append(kwargs[key])
        else:
            x_test.append(np.log10(kwargs[key]))
    x_test = np.vstack(x_test).T
    pred[cut_geometry] = self.classifier.predict_proba(x_test[cut_geometry])[:,
        (1)]
    self.validatePredict(pred, flags_geometry, lon, lat, kwargs[
        'r_physical'], kwargs['abs_mag'], kwargs['distance'])
    return pred, flags_geometry