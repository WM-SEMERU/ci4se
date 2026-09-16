def match_template(template, image, options=None):
    if len(image.shape) <= 3 and image.shape[2] <= 3:
        return match_template_opencv(template, image, options)
    op = _DEF_TM_OPT.copy()
    if options is not None:
        op.update(options)
    template = img_utils.gray3(template)
    image = img_utils.gray3(image)
    h, w, d = template.shape
    im_h, im_w = image.shape[:2]
    template_v = template.flatten()
    heatmap = np.zeros((im_h - h, im_w - w))
    for col in range(0, im_w - w):
        for row in range(0, im_h - h):
            cropped_im = image[row:row + h, col:col + w, :]
            cropped_v = cropped_im.flatten()
            if op['distance'] == 'euclidean':
                heatmap[row, col] = scipy.spatial.distance.euclidean(template_v
                    , cropped_v)
            elif op['distance'] == 'correlation':
                heatmap[row, col] = scipy.spatial.distance.correlation(
                    template_v, cropped_v)
    if op['normalize']:
        heatmap /= heatmap.max()
    if op['retain_size']:
        hmap = np.ones(image.shape[:2]) * heatmap.max()
        h, w = heatmap.shape
        hmap[:h, :w] = heatmap
        heatmap = hmap
    return heatmap