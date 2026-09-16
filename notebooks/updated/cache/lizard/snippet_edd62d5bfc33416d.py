def kl(samples1, samples2, pdf1=False, pdf2=False, bins=30, hist_min=None,
    hist_max=None):
    hist_range = hist_min, hist_max
    if not pdf1:
        samples1, _ = numpy.histogram(samples1, bins=bins, range=hist_range,
            normed=True)
    if not pdf2:
        samples2, _ = numpy.histogram(samples2, bins=bins, range=hist_range,
            normed=True)
    return stats.entropy(samples1, qk=samples2)