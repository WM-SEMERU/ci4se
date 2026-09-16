def _human_score_map(human_consensus, methods_attrs):
    v = 1 - min(np.sum(np.abs(methods_attrs - human_consensus)) / (np.abs(
        human_consensus).sum() + 1), 1.0)
    return v