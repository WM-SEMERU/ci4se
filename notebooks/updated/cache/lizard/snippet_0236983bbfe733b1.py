def parsemeta(metadataloc):
    if os.path.isdir(metadataloc):
        metalist = glob.glob(os.path.join(metadataloc, METAPATTERN))
        if not metalist:
            raise MTLParseError(
                'No files matching metadata file pattern in directory %s.' %
                metadataloc)
        elif len(metalist) > 0:
            metadatafn = metalist[0]
            filehandle = open(metadatafn, 'r')
            if len(metalist) > 1:
                logging.warning(
                    'More than one file in directory match metadata ' + 
                    'file pattern. Using %s.' % metadatafn)
    elif os.path.isfile(metadataloc):
        metadatafn = metadataloc
        filehandle = open(metadatafn, 'r')
        logging.info('Using file %s.' % metadatafn)
    elif 'L1_METADATA_FILE' in metadataloc:
        filehandle = StringIO(metadataloc)
    else:
        raise MTLParseError('File location %s is unavailable ' %
            metadataloc + "or doesn't contain a suitable metadata file.")
    status = 0
    metadata = {}
    grouppath = []
    dictpath = [metadata]
    for line in filehandle:
        if status == 4:
            logging.warning('Metadata file %s appears to ' % metadatafn +
                'have extra lines after the end of the metadata. ' +
                'This is probably, but not necessarily, harmless.')
        status = _checkstatus(status, line)
        grouppath, dictpath = _transstat(status, grouppath, dictpath, line)
    return metadata