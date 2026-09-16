def listDataTypes(self, datatype='', dataset=''):
    try:
        return self.dbsDataType.listDataType(dataType=datatype, dataset=dataset
            )
    except dbsException as de:
        dbsExceptionHandler(de.eCode, de.message, self.logger.exception, de
            .serverError)
    except Exception as ex:
        sError = (
            'DBSReaderModel/listDataTypes. %s\n. Exception trace: \n %s' %
            (ex, traceback.format_exc()))
        dbsExceptionHandler('dbsException-server-error', dbsExceptionCode[
            'dbsException-server-error'], self.logger.exception, sError)