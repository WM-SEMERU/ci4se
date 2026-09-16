def runSavedQueryByID(self, saved_query_id, returned_properties=None):
    if not isinstance(saved_query_id, six.string_types) or not saved_query_id:
        excp_msg = 'Please specify a valid saved query id'
        self.log.error(excp_msg)
        raise exception.BadValue(excp_msg)
    return self._runSavedQuery(saved_query_id, returned_properties=
        returned_properties)