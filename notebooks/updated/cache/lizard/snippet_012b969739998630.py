def imread(files, **kwargs):
    kwargs_file = parse_kwargs(kwargs, 'is_ome', 'multifile', '_useframes',
        'name', 'offset', 'size', 'multifile_close', 'fastij', 'movie')
    kwargs_seq = parse_kwargs(kwargs, 'pattern')
    if kwargs.get('pages', None) is not None:
        if kwargs.get('key', None) is not None:
            raise TypeError(
                "the 'pages' and 'key' arguments cannot be used together")
        log.warning("imread: the 'pages' argument is deprecated")
        kwargs['key'] = kwargs.pop('pages')
    if isinstance(files, basestring) and any(i in files for i in '?*'):
        files = glob.glob(files)
    if not files:
        raise ValueError('no files found')
    if not hasattr(files, 'seek') and len(files) == 1:
        files = files[0]
    if isinstance(files, basestring) or hasattr(files, 'seek'):
        with TiffFile(files, **kwargs_file) as tif:
            return tif.asarray(**kwargs)
    else:
        with TiffSequence(files, **kwargs_seq) as imseq:
            return imseq.asarray(**kwargs)