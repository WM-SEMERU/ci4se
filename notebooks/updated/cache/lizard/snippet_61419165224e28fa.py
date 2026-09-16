def gate(self, tzero=1.0, tpad=0.5, whiten=True, threshold=50.0,
    cluster_window=0.5, **whiten_kwargs):
    try:
        from scipy.signal import find_peaks
    except ImportError as exc:
        exc.args = 'Must have scipy>=1.1.0 to utilize this method.',
        raise
    data = self.whiten(**whiten_kwargs) if whiten else self
    window_samples = cluster_window * data.sample_rate.value
    gates = find_peaks(abs(data.value), height=threshold, distance=
        window_samples)[0]
    out = self.copy()
    nzero = int(abs(tzero) * self.sample_rate.value)
    npad = int(abs(tpad) * self.sample_rate.value)
    half = nzero + npad
    ntotal = 2 * half
    for gate in gates:
        left_idx = max(0, gate - half)
        right_idx = min(gate + half, len(self.value) - 1)
        left_idx_window = half - (gate - left_idx)
        right_idx_window = half + (right_idx - gate)
        window = 1 - planck(ntotal, nleft=npad, nright=npad)
        window = window[left_idx_window:right_idx_window]
        out[left_idx:right_idx] *= window
    return out