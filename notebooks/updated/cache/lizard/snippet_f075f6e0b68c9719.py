def concat_t_vars(self):
    logger.warning(
        'This function is deprecated and replaced by `concat_t_vars_np`.')
    out = np.array([])
    if len(self.t) == 0:
        return out
    out = np.ndarray(shape=(0, self.vars[0].size[0] + 1))
    for t, var in zip(self.t, self.vars):
        line = [[t]]
        line[0].extend(list(var))
        out = np.append(out, line, axis=0)
    return out