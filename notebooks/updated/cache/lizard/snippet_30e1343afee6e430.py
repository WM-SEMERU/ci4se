def trips_process_xml():
    if request.method == 'OPTIONS':
        return {}
    response = request.body.read().decode('utf-8')
    body = json.loads(response)
    xml_str = body.get('xml_str')
    tp = trips.process_xml(xml_str)
    return _stmts_from_proc(tp)