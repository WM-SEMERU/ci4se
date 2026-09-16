def changes(self):
    deprecation_msg = 'Model.changes will be removed in warlock v2'
    warnings.warn(deprecation_msg, DeprecationWarning, stacklevel=2)
    return copy.deepcopy(self.__dict__['changes'])