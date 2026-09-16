def get_cloud_probability_maps(self, X):
    band_num = X.shape[-1]
    exp_bands = 13 if self.all_bands else len(self.BAND_IDXS)
    if band_num != exp_bands:
        raise ValueError(
            "Parameter 'all_bands' is set to {}. Therefore expected band data with {} bands, got {} bands"
            .format(self.all_bands, exp_bands, band_num))
    if self.all_bands:
        X = X[..., self.BAND_IDXS]
    return self.classifier.image_predict_proba(X)[..., 1]