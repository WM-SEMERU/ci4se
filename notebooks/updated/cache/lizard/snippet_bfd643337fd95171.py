def precision_pct_pred_pos_curve(self, interval=False, delta_tau=0.001):
    orig_thresh = self.threshold
    sorted_labels, sorted_probs = self.sorted_values
    precisions = []
    pct_pred_pos = []
    taus = []
    tau = 0
    if not interval:
        for k in range(len(sorted_labels)):
            self.threshold = tau
            precisions.append(self.precision)
            pct_pred_pos.append(self.pct_pred_pos)
            taus.append(tau)
            tau = sorted_probs[k]
    else:
        while tau < 1.0:
            self.threshold = tau
            precisions.append(self.precision)
            pct_pred_pos.append(self.pct_pred_pos)
            taus.append(tau)
            tau += delta_tau
    tau = 1.0
    self.threshold = tau
    precisions.append(self.precision)
    pct_pred_pos.append(self.pct_pred_pos)
    taus.append(tau)
    precisions.append(1.0)
    pct_pred_pos.append(0.0)
    taus.append(1.0 + 1e-12)
    self.threshold = orig_thresh
    return precisions, pct_pred_pos, taus