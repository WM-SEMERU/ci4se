def chord_length_distribution(im, bins=None, log=False, voxel_size=1,
    normalization='count'):
    r
    x = chord_counts(im)
    if bins is None:
        bins = sp.array(range(0, x.max() + 2)) * voxel_size
    x = x * voxel_size
    if log:
        x = sp.log10(x)
    if normalization == 'length':
        h = list(sp.histogram(x, bins=bins, density=False))
        h[0] = h[0] * (h[1][1:] + h[1][:-1]) / 2
        h[0] = h[0] / h[0].sum() / (h[1][1:] - h[1][:-1])
    elif normalization in ['number', 'count']:
        h = sp.histogram(x, bins=bins, density=True)
    else:
        raise Exception('Unsupported normalization:', normalization)
    h = _parse_histogram(h)
    cld = namedtuple('chord_length_distribution', (log * 'log' + 'L', 'pdf',
        'cdf', 'relfreq', 'bin_centers', 'bin_edges', 'bin_widths'))
    return cld(h.bin_centers, h.pdf, h.cdf, h.relfreq, h.bin_centers, h.
        bin_edges, h.bin_widths)