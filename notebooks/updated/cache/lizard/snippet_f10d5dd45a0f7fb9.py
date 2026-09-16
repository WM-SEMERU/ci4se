def get_server_alerts(call=None, for_output=True, **kwargs):
    for key, value in kwargs.items():
        servername = ''
        if key == 'servername':
            servername = value
    creds = get_creds()
    clc.v2.SetCredentials(creds['user'], creds['password'])
    alerts = clc.v2.Server(servername).Alerts()
    return alerts