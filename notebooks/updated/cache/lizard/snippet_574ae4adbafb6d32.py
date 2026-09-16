def _makeNestedTempDir(top, seed, levels=2):
    validDirs = hashlib.md5(six.b(str(seed))).hexdigest()
    tempDir = top
    for i in range(max(min(levels, len(validDirs)), 1)):
        tempDir = os.path.join(tempDir, validDirs[i])
        if not os.path.exists(tempDir):
            try:
                os.makedirs(tempDir)
            except os.error:
                if not os.path.exists(tempDir):
                    raise
    return tempDir