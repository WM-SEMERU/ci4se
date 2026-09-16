def get_v_total_stress_at_depth(self, z):
    if not hasattr(z, '__len__'):
        return self.one_vertical_total_stress(z)
    else:
        sigma_v_effs = []
        for value in z:
            sigma_v_effs.append(self.one_vertical_total_stress(value))
        return np.array(sigma_v_effs)