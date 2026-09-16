def from_grayscale_and_depth(gray_im, depth_im):
    if gray_im.height != depth_im.height or gray_im.width != depth_im.width:
        raise ValueError('Grayscale and depth images must have the same shape')
    if gray_im.frame != depth_im.frame:
        raise ValueError('Grayscale and depth images must have the same frame')
    gd_data = np.zeros([gray_im.height, gray_im.width, 2])
    gd_data[:, :, (0)] = gray_im.data.astype(np.float64)
    gd_data[:, :, (1)] = depth_im.data
    return GdImage(gd_data, frame=gray_im.frame)