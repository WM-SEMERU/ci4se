def runSavedQuery(self, saved_query_obj, returned_properties=None):
    try:
        saved_query_id = saved_query_obj.results.split('/')[-2]
    except:
        error_msg = 'Cannot get the correct saved query id'
        self.log.error(error_msg)
        raise exception.RTCException(error_msg)
    return self._runSavedQuery(saved_query_id, returned_properties=
        returned_properties)