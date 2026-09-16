def find_outer_region(im, r=0):
    r
    if r == 0:
        dt = spim.distance_transform_edt(input=im)
        r = int(sp.amax(dt)) * 2
    im_padded = sp.pad(array=im, pad_width=r, mode='constant',
        constant_values=True)
    dt = spim.distance_transform_edt(input=im_padded)
    seeds = (dt >= r) + get_border(shape=im_padded.shape)
    labels = spim.label(seeds)[0]
    mask = labels == 1
    dt = spim.distance_transform_edt(~mask)
    outer_region = dt < r
    outer_region = extract_subsection(im=outer_region, shape=im.shape)
    return outer_region