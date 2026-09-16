def batchsd(trace, batches=5):
    if len(np.shape(trace)) > 1:
        dims = np.shape(trace)
        ttrace = np.transpose([t.ravel() for t in trace])
        return np.reshape([batchsd(t, batches) for t in ttrace], dims[1:])
    else:
        if batches == 1:
            return np.std(trace) / np.sqrt(len(trace))
        try:
            batched_traces = np.resize(trace, (batches, int(len(trace) /
                batches)))
        except ValueError:
            resid = len(trace) % batches
            batched_traces = np.resize(trace[:-resid], (batches, len(trace[
                :-resid]) / batches))
        means = np.mean(batched_traces, 1)
        return np.std(means) / np.sqrt(batches)