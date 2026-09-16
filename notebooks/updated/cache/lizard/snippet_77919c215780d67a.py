def fetch_logs(self, max_rows=1024, orientation=None):
    from pyhive import hive
    from TCLIService import ttypes
    from thrift import Thrift
    orientation = orientation or ttypes.TFetchOrientation.FETCH_NEXT
    try:
        req = ttypes.TGetLogReq(operationHandle=self._operationHandle)
        logs = self._connection.client.GetLog(req).log
        return logs
    except (ttypes.TApplicationException, Thrift.TApplicationException):
        if self._state == self._STATE_NONE:
            raise hive.ProgrammingError('No query yet')
        logs = []
        while True:
            req = ttypes.TFetchResultsReq(operationHandle=self.
                _operationHandle, orientation=ttypes.TFetchOrientation.
                FETCH_NEXT, maxRows=self.arraysize, fetchType=1)
            response = self._connection.client.FetchResults(req)
            hive._check_status(response)
            assert not response.results.rows, 'expected data in columnar format'
            assert len(response.results.columns) == 1, response.results.columns
            new_logs = hive._unwrap_column(response.results.columns[0])
            logs += new_logs
            if not new_logs:
                break
        return '\n'.join(logs)