def _amp2d_to_3d(self, amp, sigma_x, sigma_y):
    return amp / (np.sqrt(np.pi) * np.sqrt(sigma_x * sigma_y * 2))