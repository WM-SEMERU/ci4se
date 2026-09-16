def ReadFlowResults(self, client_id, flow_id, offset, count, with_tag=None,
    with_type=None, with_substring=None, cursor=None):
    query = (
        'SELECT payload, type, UNIX_TIMESTAMP(timestamp), tag FROM flow_results FORCE INDEX (flow_results_by_client_id_flow_id_timestamp) WHERE client_id = %s AND flow_id = %s '
        )
    args = [db_utils.ClientIDToInt(client_id), db_utils.FlowIDToInt(flow_id)]
    if with_tag is not None:
        query += 'AND tag = %s '
        args.append(with_tag)
    if with_type is not None:
        query += 'AND type = %s '
        args.append(with_type)
    if with_substring is not None:
        query += 'AND payload LIKE %s '
        args.append('%{}%'.format(with_substring))
    query += 'ORDER BY timestamp ASC LIMIT %s OFFSET %s'
    args.append(count)
    args.append(offset)
    cursor.execute(query, args)
    ret = []
    for serialized_payload, payload_type, ts, tag in cursor.fetchall():
        if payload_type in rdfvalue.RDFValue.classes:
            payload = rdfvalue.RDFValue.classes[payload_type]()
            payload.ParseFromString(serialized_payload)
        else:
            payload = rdf_objects.SerializedValueOfUnrecognizedType(type_name
                =payload_type, value=serialized_payload)
        timestamp = mysql_utils.TimestampToRDFDatetime(ts)
        result = rdf_flow_objects.FlowResult(payload=payload, timestamp=
            timestamp)
        if tag:
            result.tag = tag
        ret.append(result)
    return ret