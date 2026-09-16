def _updateHiddenStateTrajectories(self):
    self.model.hidden_state_trajectories = list()
    for trajectory_index in range(self.nobs):
        hidden_state_trajectory = self._sampleHiddenStateTrajectory(self.
            observations[trajectory_index])
        self.model.hidden_state_trajectories.append(hidden_state_trajectory)
    return