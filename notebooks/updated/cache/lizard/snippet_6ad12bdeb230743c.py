def ReadChildFlowObjects(self, client_id, flow_id, cursor=None):
    query = ('SELECT ' + self.FLOW_DB_FIELDS +
        'FROM flows WHERE client_id=%s AND parent_flow_id=%s')
    cursor.execute(query, [db_utils.ClientIDToInt(client_id), db_utils.
        FlowIDToInt(flow_id)])
    return [self._FlowObjectFromRow(row) for row in cursor.fetchall()]