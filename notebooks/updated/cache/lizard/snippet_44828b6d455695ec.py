def single_feature_fit(self, feature):
    if np.isfinite(feature).sum() == 0:
        series = pd.Series(index=MODALITY_ORDER)
    else:
        logbf_one_param = pd.Series({k: v.logsumexp_logliks(feature) for k,
            v in self.one_param_models.items()})
        if (logbf_one_param <= self.logbf_thresh).all():
            logbf_two_param = pd.Series({k: v.logsumexp_logliks(feature) for
                k, v in self.two_param_models.items()})
            series = pd.concat([logbf_one_param, logbf_two_param])
            series[NULL_MODEL] = self.logbf_thresh
        else:
            series = logbf_one_param
    series.index.name = 'Modality'
    series.name = self.score_name
    return series