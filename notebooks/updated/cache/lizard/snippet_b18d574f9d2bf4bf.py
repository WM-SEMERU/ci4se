def new(image):
    pointer = vips_lib.vips_region_new(image.pointer)
    if pointer == ffi.NULL:
        raise Error('unable to make region')
    return pyvips.Region(pointer)