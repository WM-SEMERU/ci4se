def _get_image_paths(im1, im2):
    paths = []
    for im in [im1, im2]:
        if im is None:
            paths.append(paths[0])
            continue
        if isinstance(im, str):
            if os.path.isfile(im1):
                paths.append(im)
            else:
                raise ValueError('Image location does not exist.')
        elif isinstance(im, np.ndarray):
            id = len(paths) + 1
            p = _write_image_data(im, id)
            paths.append(p)
        else:
            raise ValueError('Invalid input image.')
    return tuple(paths)