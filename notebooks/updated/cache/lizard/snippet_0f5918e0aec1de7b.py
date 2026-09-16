def get_func(name, argtypes=None, restype=c_int, lib=libNLPIR):
    logger.debug(
        "Getting NLPIR API function: 'name': '{}', 'argtypes': '{}', 'restype': '{}'."
        .format(name, argtypes, restype))
    func = getattr(lib, name)
    if argtypes is not None:
        func.argtypes = argtypes
    if restype is not c_int:
        func.restype = restype
    logger.debug("NLPIR API function '{}' retrieved.".format(name))
    return func