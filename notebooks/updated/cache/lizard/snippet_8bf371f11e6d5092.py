def get_numpy_type(dicom_header):
    format_string = '%sint%d' % (('u', '')[dicom_header.PixelRepresentation
        ], dicom_header.BitsAllocated)
    try:
        numpy.dtype(format_string)
    except TypeError:
        raise TypeError(
            "Data type not understood by NumPy: format='%s', PixelRepresentation=%d, BitsAllocated=%d"
             % (format_string, dicom_header.PixelRepresentation,
            dicom_header.BitsAllocated))
    return format_string