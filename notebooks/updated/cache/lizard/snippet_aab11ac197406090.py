def get_subs_dict(self, qnodes=None):
    d = self.qparams
    d.update(self.optimize_params(qnodes=qnodes))
    subs_dict = {k: v for k, v in d.items() if v is not None}
    return subs_dict