def interpolate_exe(self, testString):
    testString = testString.strip()
    if not (testString.startswith('${') and testString.endswith('}')):
        return testString
    newString = testString
    testString = testString[2:-1]
    testList = testString.split(':')
    if len(testList) == 2:
        if testList[0] == 'which':
            newString = distutils.spawn.find_executable(testList[1])
            if not newString:
                errmsg = 'Cannot find exe %s in your path ' % testList[1]
                errmsg += 'and you specified ${which:%s}.' % testList[1]
                raise ValueError(errmsg)
    return newString