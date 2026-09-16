def load_libdmtx():
    global LIBDMTX
    global EXTERNAL_DEPENDENCIES
    if not LIBDMTX:
        LIBDMTX = dmtx_library.load()
        EXTERNAL_DEPENDENCIES = [LIBDMTX]
    return LIBDMTX