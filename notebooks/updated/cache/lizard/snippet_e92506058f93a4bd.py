def display_scores(params, scores, append_star=False):
    params = ', '.join('{0}={1}'.format(k, v) for k, v in params.items())
    line = '{0}:\t\t{1:.3f} (+/-{2:.3f})'.format(params, np.mean(scores),
        sem(scores))
    if append_star:
        line += ' *'
    return line