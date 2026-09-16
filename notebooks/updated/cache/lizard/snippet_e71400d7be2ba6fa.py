def listFileChildren(self, logical_file_name='', block_name='', block_id=0):
    if isinstance(logical_file_name, list):
        for f in logical_file_name:
            if '*' in f or '%' in f:
                dbsExceptionHandler('dbsException-invalid-input2',
                    dbsExceptionCode['dbsException-invalid-input2'], self.
                    logger.exception,
                    'No                                          wildcard allow in LFN list'
                    )
    try:
        return self.dbsFile.listFileChildren(logical_file_name, block_name,
            block_id)
    except dbsException as de:
        dbsExceptionHandler(de.eCode, de.message, self.logger.exception, de
            .serverError)
    except Exception as ex:
        sError = (
            'DBSReaderModel/listFileChildren. %s\n. Exception trace: \n %s' %
            (ex, traceback.format_exc()))
        dbsExceptionHandler('dbsException-server-error', dbsExceptionCode[
            'dbsException-server-error'], self.logger.exception, sError)