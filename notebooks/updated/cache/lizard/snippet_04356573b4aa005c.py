def append(self, listname, xy_idx, var_name, element_name):
    self.resize()
    string = '{0} {1}'
    if listname not in ['unamex', 'unamey', 'fnamex', 'fnamey']:
        logger.error('Wrong list name for varname.')
        return
    elif listname in ['fnamex', 'fnamey']:
        string = '${0}\\ {1}$'
    if isinstance(element_name, list):
        for i, j in zip(xy_idx, element_name):
            if listname == 'fnamex' or listname == 'fnamey':
                j = j.replace(' ', '\\ ')
            self.__dict__[listname][i] = string.format(var_name, j)
    elif isinstance(element_name, int):
        self.__dict__[listname][xy_idx] = string.format(var_name, element_name)
    else:
        logger.warning('Unknown element_name type while building varname')