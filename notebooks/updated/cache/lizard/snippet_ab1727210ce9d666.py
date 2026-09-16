def precision_at_proportions(self):
    return plot.precision_at_proportions(self.y_true, self.y_score, ax=
        _gen_ax())