def _readBatchOutputForFile(self, directory, fileIO, filename, session,
    spatial, spatialReferenceID, replaceParamFile=None, maskMap=None):
    directoryList = os.listdir(directory)
    batchFiles = []
    for thing in directoryList:
        if filename in thing:
            batchFiles.append(thing)
    numFilesRead = 0
    for batchFile in batchFiles:
        instance = fileIO()
        instance.projectFile = self
        if isinstance(instance, WMSDatasetFile):
            instance.read(directory=directory, filename=batchFile, session=
                session, maskMap=maskMap, spatial=spatial,
                spatialReferenceID=spatialReferenceID)
        else:
            instance.read(directory, batchFile, session, spatial=spatial,
                spatialReferenceID=spatialReferenceID, replaceParamFile=
                replaceParamFile)
        numFilesRead += 1
    if '[' in filename or ']' in filename:
        log.info(
            'A file cannot be read, because the path to the file in the project file has been replaced with replacement variable {0}.'
            .format(filename))
    elif numFilesRead == 0:
        log.warning('{0} listed in project file, but no such file exists.'.
            format(filename))
    else:
        log.info('Batch mode output detected. {0} files read for file {1}'.
            format(numFilesRead, filename))