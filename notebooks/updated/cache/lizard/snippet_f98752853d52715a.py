def predictions(self, setup, n_jobs=-1):
    stimuli, inhibitors, readouts = (setup.stimuli, setup.inhibitors, setup
        .readouts)
    nc = len(setup.cues())
    predictions = np.zeros((len(self), 2 ** nc, len(setup)))
    predictions[:, :, :] = Parallel(n_jobs=n_jobs)(delayed(
        __parallel_predictions__)(n, list(setup.clampings_iter(setup.cues()
        )), readouts, stimuli, inhibitors) for n in self)
    avg = np.average(predictions[:, :, nc:], axis=0, weights=self.__networks)
    var = np.average((predictions[:, :, nc:] - avg) ** 2, axis=0, weights=
        self.__networks)
    rcues = [('TR:%s' % c) for c in setup.cues(True)]
    cols = np.concatenate([rcues, [('AVG:%s' % r) for r in readouts], [(
        'VAR:%s' % r) for r in readouts]])
    df = pd.DataFrame(np.concatenate([predictions[(0), :, :nc], avg, var],
        axis=1), columns=cols)
    df[rcues] = df[rcues].astype(int)
    return df