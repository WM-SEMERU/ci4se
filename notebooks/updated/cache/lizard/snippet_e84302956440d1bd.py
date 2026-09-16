def graphcut_stawiaski(regions, gradient=False, foreground=False,
    background=False):
    logger = Logger.getInstance()
    if not gradient and not foreground and not background:
        regions, gradient, foreground, background = regions
    img_region = scipy.asarray(regions)
    img_gradient = scipy.asarray(gradient)
    img_fg = scipy.asarray(foreground, dtype=scipy.bool_)
    img_bg = scipy.asarray(background, dtype=scipy.bool_)
    if (not img_region.shape == img_gradient.shape == img_fg.shape ==
        img_bg.shape):
        raise ArgumentError('All supplied images must be of the same shape.')
    img_region = relabel(img_region)
    gcgraph = graph_from_labels(img_region, img_fg, img_bg, boundary_term=
        boundary_stawiaski, boundary_term_args=img_gradient)
    maxflow = gcgraph.maxflow()
    logger.debug('Graph-cut terminated successfully with maxflow of {}.'.
        format(maxflow))
    mapping = [0]
    mapping.extend([(0 if gcgraph.termtype.SINK == gcgraph.what_segment(int
        (x) - 1) else 1) for x in scipy.unique(img_region)])
    img_results = relabel_map(img_region, mapping)
    return img_results.astype(scipy.bool_)