def getTypeInfo(self, sql_type):
    fut = self._run_operation(self._impl.getTypeInfo, sql_type)
    return fut