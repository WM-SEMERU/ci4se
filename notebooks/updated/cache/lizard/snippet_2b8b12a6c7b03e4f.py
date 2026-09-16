def get_by_request_id(env, request_id):
    mgr = SoftLayer.NetworkManager(env.client)
    logs = mgr.get_event_logs_by_request_id(request_id)
    table = formatting.Table(COLUMNS)
    table.align['metadata'] = 'l'
    for log in logs:
        metadata = json.dumps(json.loads(log['metaData']), indent=4,
            sort_keys=True)
        table.add_row([log['eventName'], log['label'], log[
            'eventCreateDate'], metadata])
    env.fout(table)