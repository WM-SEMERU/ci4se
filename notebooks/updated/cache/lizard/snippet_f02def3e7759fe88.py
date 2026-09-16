def _mean_prediction(self, theta, theta_t, Y, scores, h, t_params):
    Y_exp = Y.copy()
    theta_exp = theta.copy()
    theta_t_exp = theta_t.copy()
    scores_exp = scores.copy()
    for t in range(0, h):
        new_value1 = theta_t_exp[-1] + theta_exp[-1] + t_params[0
            ] * scores_exp[-1]
        new_value2 = theta_t_exp[-1] + t_params[1] * scores_exp[-1]
        if self.model_name2 == 'Exponential':
            Y_exp = np.append(Y_exp, [1.0 / self.link(new_value1)])
        else:
            Y_exp = np.append(Y_exp, [self.link(new_value1)])
        theta_exp = np.append(theta_exp, [new_value1])
        theta_t_exp = np.append(theta_t_exp, [new_value2])
        scores_exp = np.append(scores_exp, [0])
    return Y_exp