def _getAllJobStates(workflowDir):
    jobStateFiles = []
    for root, dirs, files in os.walk(workflowDir):
        for filename in files:
            if filename == '.jobState':
                jobStateFiles.append(os.path.join(root, filename))
    for filename in jobStateFiles:
        try:
            yield NonCachingFileStore._readJobState(filename)
        except IOError as e:
            if e.errno == 2:
                continue
            else:
                raise