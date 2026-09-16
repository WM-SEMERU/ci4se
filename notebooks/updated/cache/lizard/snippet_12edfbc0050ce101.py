def unit_choice(chooser_ids, alternative_ids, probabilities):
    chooser_ids = np.asanyarray(chooser_ids)
    alternative_ids = np.asanyarray(alternative_ids)
    probabilities = np.asanyarray(probabilities)
    logger.debug('start: unit choice with {} choosers and {} alternatives'.
        format(len(chooser_ids), len(alternative_ids)))
    choices = pd.Series(index=chooser_ids)
    if probabilities.sum() == 0:
        return choices
    probabilities = probabilities / probabilities.sum()
    n_available = np.count_nonzero(probabilities)
    n_choosers = len(chooser_ids)
    n_to_choose = n_choosers if n_choosers < n_available else n_available
    chosen = np.random.choice(alternative_ids, size=n_to_choose, replace=
        False, p=probabilities)
    if n_to_choose == n_available:
        chooser_ids = np.random.choice(chooser_ids, size=n_to_choose,
            replace=False)
    choices[chooser_ids] = chosen
    logger.debug('finish: unit choice')
    return choices