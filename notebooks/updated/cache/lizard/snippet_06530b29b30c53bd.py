def extract_ref(scihdu, refhdu):
    same_size, rx, ry, x0, y0 = find_line(scihdu, refhdu)
    if same_size:
        return refhdu.data
    if rx != 1 or ry != 1:
        raise NotImplementedError('Either science or reference data are binned'
            )
    ny, nx = scihdu.data.shape
    refdata = refhdu.data[y0:y0 + ny, x0:x0 + nx]
    if refdata.shape != (ny, nx):
        raise ValueError(
            'Extracted reference image is {0} but science image is {1}'.
            format(refdata.shape, (ny, nx)))
    return refdata