def getParamValues(self, paramName=None, paramId=None, useOnlyValids=True):
    if not paramName is None:
        if not paramId is None:
            if getParameterTypeNameFromID(paramId) != paramName:
                raise ValueError('Parameters paramId and paramName ' +
                    'passed to ParamSample.getParamValues() are incompatible.')
    else:
        if paramId is None:
            raise ValueError(
                'At least one of the attribute paramName and paramId ' +
                'passed to ParamSample.getParamValues() most not be None.')
        paramName = getParameterTypeNameFromID(paramId)
    df = self.sampleDF
    if useOnlyValids:
        df = df[df['isValid'] == True]
    df.loc[:, ('paramNames')] = [getParameterTypeNameFromID(param.typeId) for
        param in df['obj_parameter']]
    return df[df['paramNames'] == paramName]