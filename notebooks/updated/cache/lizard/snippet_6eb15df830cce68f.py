def updateComponentStartVals(self):
    for param in self._parameters:
        for component in param['selection']:
            if param['parameter'] == 'filename':
                component.set(param['parameter'], param['names'][0])
            else:
                component.set(param['parameter'], param['start'])