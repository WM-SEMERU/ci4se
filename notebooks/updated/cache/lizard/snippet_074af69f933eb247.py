def number_cwt_peaks(x, n):
    return len(find_peaks_cwt(vector=x, widths=np.array(list(range(1, n + 1
        ))), wavelet=ricker))