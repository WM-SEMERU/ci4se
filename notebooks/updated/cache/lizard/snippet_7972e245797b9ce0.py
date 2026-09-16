def app_score(self):
    precisions, pct_pred_pos, taus = self.precision_pct_pred_pos_curve(interval
        =False)
    app = 0
    total = 0
    for k in range(len(precisions) - 1):
        cur_prec = precisions[k]
        cur_pp = pct_pred_pos[k]
        cur_tau = taus[k]
        next_prec = precisions[k + 1]
        next_pp = pct_pred_pos[k + 1]
        next_tau = taus[k + 1]
        mid_prec = (cur_prec + next_prec) / 2.0
        width_pp = np.abs(next_pp - cur_pp)
        app += mid_prec * width_pp
        total += width_pp
    return app