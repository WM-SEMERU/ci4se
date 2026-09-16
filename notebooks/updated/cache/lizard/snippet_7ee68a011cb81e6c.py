def _processDatatypes(self, rm, ci, smi, sai, si):
    datatypes = list()
    for datatype, value in [('rm', rm), ('ci', ci), ('smi', smi), ('sai',
        sai), ('si', si)]:
        if value:
            datatypes.append(datatype)
    return datatypes