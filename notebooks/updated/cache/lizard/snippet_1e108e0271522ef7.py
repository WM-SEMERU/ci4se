def Cinv(self):
    try:
        return np.linalg.inv(self.c)
    except np.linalg.linalg.LinAlgError:
        print('Warning: non-invertible noise covariance matrix c.')
        return np.eye(self.c.shape[0])