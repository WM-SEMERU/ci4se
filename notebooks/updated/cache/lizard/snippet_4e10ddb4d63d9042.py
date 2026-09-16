def printDuplicatedTPEDandTFAM(tped, tfamFileName, outPrefix):
    try:
        shutil.copy(tfamFileName, outPrefix + '.duplicated_snps.tfam')
    except IOError:
        msg = (
            "%(tfamFileName)s: can't copy file to %(outPrefix)s.duplicated_snps.tfam"
             % locals())
        raise ProgramError(msg)
    tpedFile = None
    try:
        tpedFile = open(outPrefix + '.duplicated_snps.tped', 'w')
    except IOError:
        msg = "%(outPrefix)s.duplicated_snps.tped: can't write file" % locals()
        raise ProgramError(msg)
    for row in tped:
        print >> tpedFile, '\t'.join(row)
    tpedFile.close()