def _getOpenChoices(self):
    tsk = self._taskParsObj.getName()
    taskFiles = set()
    dirsSoFar = []
    aDir = os.path.dirname(self._taskParsObj.filename)
    if len(aDir) < 1:
        aDir = os.curdir
    dirsSoFar.append(aDir)
    taskFiles.update(cfgpars.getCfgFilesInDirForTask(aDir, tsk))
    aDir = os.getcwd()
    if aDir not in dirsSoFar:
        dirsSoFar.append(aDir)
        taskFiles.update(cfgpars.getCfgFilesInDirForTask(aDir, tsk))
    try:
        x, pkgf = cfgpars.findCfgFileForPkg(tsk, '.cfg', taskName=tsk,
            pkgObj=self._taskParsObj.getAssocPkg())
        taskFiles.update((pkgf,))
    except cfgpars.NoCfgFileError:
        pass
    aDir = self._rcDir
    if aDir not in dirsSoFar:
        dirsSoFar.append(aDir)
        taskFiles.update(cfgpars.getCfgFilesInDirForTask(aDir, tsk))
    aDir = dirsSoFar[0]
    envVarName = APP_NAME.upper() + '_CFG'
    if envVarName in os.environ:
        aDir = os.environ[envVarName]
    if aDir not in dirsSoFar:
        dirsSoFar.append(aDir)
        taskFiles.update(cfgpars.getCfgFilesInDirForTask(aDir, tsk))
    taskFiles = list(taskFiles)
    taskFiles.sort()
    taskFiles.append('Other ...')
    return taskFiles