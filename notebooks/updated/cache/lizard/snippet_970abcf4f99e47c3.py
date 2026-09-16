def _compute_smooth_during_construction(self, xi):
    if self._variance_in_window:
        beta = self._covariance_in_window / self._variance_in_window
        alpha = self._mean_y_in_window - beta * self._mean_x_in_window
        value_of_smooth_here = beta * xi + alpha
    else:
        value_of_smooth_here = 0.0
    return value_of_smooth_here