def imread(filename, *args, **kwargs):
    try:
        netpbm = NetpbmFile(filename)
        image = netpbm.asarray()
    finally:
        netpbm.close()
    return image