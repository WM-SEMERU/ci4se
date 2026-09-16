def sub_hmm(self, states):
    r
    pi_sub = self._Pi[states]
    pi_sub /= pi_sub.sum()
    P_sub = self._Tij[(states), :][:, (states)]
    assert np.all(P_sub.sum(axis=1) > 0
        ), 'Illegal sub_hmm request: transition matrix cannot be normalized on ' + str(
        states)
    P_sub /= P_sub.sum(axis=1)[:, (None)]
    out_sub = self.output_model.sub_output_model(states)
    return HMM(pi_sub, P_sub, out_sub, lag=self.lag)