def _CheckSQLite3(self):
    module_name = 'pysqlite2.dbapi2'
    minimum_version = '3.7.8'
    module_object = self._ImportPythonModule(module_name)
    if not module_object:
        module_name = 'sqlite3'
    module_object = self._ImportPythonModule(module_name)
    if not module_object:
        status_message = 'missing: {0:s}.'.format(module_name)
        return False, status_message
    return self._CheckPythonModuleVersion(module_name, module_object,
        'sqlite_version', minimum_version, None)