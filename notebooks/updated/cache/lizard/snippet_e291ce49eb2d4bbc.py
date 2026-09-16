def getWorkflowDir(workflowID, configWorkDir=None):
    workDir = configWorkDir or os.getenv('TOIL_WORKDIR'
        ) or tempfile.gettempdir()
    if not os.path.exists(workDir):
        raise RuntimeError(
            'The directory specified by --workDir or TOIL_WORKDIR (%s) does not exist.'
             % workDir)
    workflowDir = os.path.join(workDir, 'toil-%s-%s' % (workflowID,
        getNodeID()))
    try:
        os.mkdir(workflowDir)
    except OSError as err:
        if err.errno != 17:
            raise
    else:
        logger.debug('Created the workflow directory at %s' % workflowDir)
    return workflowDir