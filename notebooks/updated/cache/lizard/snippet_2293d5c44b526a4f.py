def gen_goal(self, y_des):
    goal = np.zeros(self.dmps)
    for n in range(self.dmps):
        num_idx = ~np.isnan(y_des[n])
        goal[n] = 0.5 * (y_des[n, num_idx].min() + y_des[n, num_idx].max())
    return goal