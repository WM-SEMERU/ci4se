def calc_query(self):
    if self.query_dist is None:
        self.query_dist = self.exp4p_.next(-1, None, None)
    else:
        self.query_dist = self.exp4p_.next(self.calc_reward_fn(), self.
            queried_hist_[-1], self.dataset.data[self.queried_hist_[-1]][1])
    return