def compute(self, x):
    q_learning = copy(self.__greedy_q_learning)
    q_learning.epsilon_greedy_rate = x[0]
    q_learning.alpha_value = x[1]
    q_learning.gamma_value = x[2]
    if self.__init_state_key is not None:
        q_learning.learn(state_key=self.__init_state_key, limit=int(x[3]))
    else:
        q_learning.learn(limit=x[3])
    q_sum = q_learning.q_df.q_value.sum()
    if q_sum != 0:
        cost = q_learning.q_df.shape[0] / q_sum
    else:
        cost = q_learning.q_df.shape[0] / 0.0001
    return cost