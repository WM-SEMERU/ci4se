def set_result(self, result, separator=''):
    if self.one_line():
        self.configs['result'] = str(result).replace('\n', separator)
    else:
        self.configs['result'] = str(result)