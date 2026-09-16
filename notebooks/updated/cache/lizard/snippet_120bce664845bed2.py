def __load_jco(self):
    if self.jco_arg is None:
        return None
    if isinstance(self.jco_arg, Matrix):
        self.__jco = self.jco_arg
    elif isinstance(self.jco_arg, str):
        self.__jco = self.__fromfile(self.jco_arg, astype=Jco)
    else:
        raise Exception('linear_analysis.__load_jco(): jco_arg must ' +
            'be a matrix object or a file name: ' + str(self.jco_arg))