def ReadMessageHandlerRequests(self, cursor=None):
    query = (
        'SELECT UNIX_TIMESTAMP(timestamp), request,       UNIX_TIMESTAMP(leased_until), leased_by FROM message_handler_requests ORDER BY timestamp DESC'
        )
    cursor.execute(query)
    res = []
    for timestamp, request, leased_until, leased_by in cursor.fetchall():
        req = rdf_objects.MessageHandlerRequest.FromSerializedString(request)
        req.timestamp = mysql_utils.TimestampToRDFDatetime(timestamp)
        req.leased_by = leased_by
        req.leased_until = mysql_utils.TimestampToRDFDatetime(leased_until)
        res.append(req)
    return res