def join_path(*path_to_join, **kwargs):
    if 'get_root' in kwargs:
        get_root = kwargs['get_root']
    else:
        get_root = False
    sdp = dataset_path(get_root=get_root)
    pth = os.path.join(sdp, *path_to_join)
    logger.debug('sample_data_path' + str(sdp))
    logger.debug('path ' + str(pth))
    return pth