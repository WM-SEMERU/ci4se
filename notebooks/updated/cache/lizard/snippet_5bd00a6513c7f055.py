def get_scores(self, *args):

    def jelinek_mercer_smoothing(cat):
        p_hat_w = self.tdf_[cat] * 1.0 / self.tdf_[cat].sum()
        c_hat_w = self.smoothing_lambda_ * self.tdf_.sum(axis=1
            ) * 1.0 / self.tdf_.sum().sum()
        return (1 - self.smoothing_lambda_
            ) * p_hat_w + self.smoothing_lambda_ * c_hat_w
    p_w = jelinek_mercer_smoothing('cat')
    q_w = jelinek_mercer_smoothing('ncat')
    kl_divergence = p_w * np.log(p_w / q_w) / np.log(2)
    tt, pvals = self.get_t_statistics()
    return kl_divergence * (pvals < self.min_p_)