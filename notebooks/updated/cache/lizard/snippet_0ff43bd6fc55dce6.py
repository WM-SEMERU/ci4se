def Hk(self, k, m_pred, P_pred):
    return self.H[:, :, (int(self.index[self.H_time_var_index, k]))]