def timeseries_to_matrix(image, mask=None):
    temp = utils.ndimage_to_list(image)
    if mask is None:
        mask = temp[0] * 0 + 1
    return image_list_to_matrix(temp, mask)