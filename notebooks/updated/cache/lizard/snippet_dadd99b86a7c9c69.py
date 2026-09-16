def _mean_dict(dict_list):
    return {k: np.array([d[k] for d in dict_list]).mean() for k in
        dict_list[0].keys()}