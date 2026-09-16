def build_histogram(data, colorscale=None, nbins=10):
    if colorscale is None:
        colorscale = colorscale_default
    colorscale = _colors_to_rgb(colorscale)
    h_min, h_max = 0, 1
    hist, bin_edges = np.histogram(data, range=(h_min, h_max), bins=nbins)
    bin_mids = np.mean(np.array(list(zip(bin_edges, bin_edges[1:]))), axis=1)
    histogram = []
    max_bucket_value = max(hist)
    sum_bucket_value = sum(hist)
    for bar, mid in zip(hist, bin_mids):
        height = np.floor(bar / max_bucket_value * 100 + 0.5)
        perc = round(bar / sum_bucket_value * 100.0, 1)
        color = _map_val2color(mid, 0.0, 1.0, colorscale)
        histogram.append({'height': height, 'perc': perc, 'color': color})
    return histogram