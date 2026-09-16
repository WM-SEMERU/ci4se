def _loss_lr_subject(self, data, labels, w, theta, bias):
    if data is None:
        return 0.0
    samples = data.shape[1]
    thetaT_wi_zi_plus_bias = theta.T.dot(w.T.dot(data)) + bias
    sum_exp, max_value, _ = utils.sumexp_stable(thetaT_wi_zi_plus_bias)
    sum_exp_values = np.log(sum_exp) + max_value
    aux = 0.0
    for sample in range(samples):
        label = labels[sample]
        aux += thetaT_wi_zi_plus_bias[label, sample]
    return self.alpha / samples / self.gamma * (sum_exp_values.sum() - aux)