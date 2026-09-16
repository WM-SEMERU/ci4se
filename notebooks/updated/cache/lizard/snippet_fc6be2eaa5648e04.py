def load_image_from_disk(img_spec):
    if isinstance(img_spec, str):
        if pexists(realpath(img_spec)):
            hdr = nib.load(img_spec)
            hdr = nib.as_closest_canonical(hdr)
            img = hdr.get_data()
        else:
            raise IOError('Given path to image does not exist!')
    elif isinstance(img_spec, np.ndarray):
        img = img_spec
    else:
        raise ValueError(
            'Invalid input specified! Input either a path to image data, or provide 3d Matrix directly.'
            )
    return img