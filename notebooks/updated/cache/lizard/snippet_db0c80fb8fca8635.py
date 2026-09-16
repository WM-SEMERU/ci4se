def get_maximum_correlation_threshold(image, mask=None, bins=256):
    if mask is not None:
        image = image[mask]
    image = image.ravel()
    nm = len(image)
    if nm == 0:
        return 0
    min_value = np.min(image)
    max_value = np.max(image)
    if min_value == max_value:
        return min_value
    image = ((image - min_value) * (bins - 1) / (max_value - min_value)
        ).astype(int)
    histogram = np.bincount(image)
    mean_value = np.mean(image)
    diff = np.arange(len(histogram)) - mean_value
    diff2 = diff * diff
    ndiff = histogram * diff
    ndiff2 = histogram * diff2
    sndiff2 = np.sum(ndiff2)
    cndiff = np.cumsum(ndiff)
    numerator = np.hstack([[cndiff[-1]], cndiff[-1] - cndiff[:-1]])
    ni = nm - np.hstack([[0], np.cumsum(histogram[:-1])])
    denominator = np.sqrt(sndiff2 * (nm - ni) * ni / nm)
    mct = numerator / denominator
    mct[denominator == 0] = 0
    my_bin = np.argmax(mct) - 1
    return min_value + my_bin * (max_value - min_value) / (bins - 1)