def delete_action(self, action, player_idx=0):
    payoff_array_new = np.delete(self.payoff_array, action, player_idx)
    return Player(payoff_array_new)