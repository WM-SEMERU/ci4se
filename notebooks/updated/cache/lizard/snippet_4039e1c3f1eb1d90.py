def ExecQuery(self, QueryLanguage, Query, namespace=None, **extra):
    exc = None
    instances = None
    method_name = 'ExecQuery'
    if self._operation_recorders:
        self.operation_recorder_reset()
        self.operation_recorder_stage_pywbem_args(method=method_name,
            QueryLanguage=QueryLanguage, Query=Query, namespace=namespace,
            **extra)
    try:
        stats = self.statistics.start_timer(method_name)
        namespace = self._iparam_namespace_from_namespace(namespace)
        result = self._imethodcall(method_name, namespace, QueryLanguage=
            QueryLanguage, Query=Query, **extra)
        if result is None:
            instances = []
        else:
            instances = [x[2] for x in result[0][2]]
        for instance in instances:
            instance.path.namespace = namespace
        return instances
    except (CIMXMLParseError, XMLParseError) as exce:
        exce.request_data = self.last_raw_request
        exce.response_data = self.last_raw_reply
        exc = exce
        raise
    except Exception as exce:
        exc = exce
        raise
    finally:
        self._last_operation_time = stats.stop_timer(self.last_request_len,
            self.last_reply_len, self.last_server_response_time, exc)
        if self._operation_recorders:
            self.operation_recorder_stage_result(instances, exc)