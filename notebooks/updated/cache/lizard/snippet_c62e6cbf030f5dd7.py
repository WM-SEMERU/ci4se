def append(self, value):
    if self.__dict__['values']:
        self.__dict__['changetype'] = MODIFY_REPLACE
    self.__dict__['values'].append(value)