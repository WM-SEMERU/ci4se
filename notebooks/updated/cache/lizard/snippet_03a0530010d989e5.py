def start_transaction(hostname, username, password, label):
    bigip_session = _build_session(username, password)
    payload = {}
    try:
        response = bigip_session.post(BIG_IP_URL_BASE.format(host=hostname) +
            '/transaction', data=salt.utils.json.dumps(payload))
    except requests.exceptions.ConnectionError as e:
        return _load_connection_error(hostname, e)
    data = _load_response(response)
    if data['code'] == 200:
        trans_id = data['content']['transId']
        __salt__['grains.setval']('bigip_f5_trans', {label: trans_id})
        return (
            'Transaction: {trans_id} - has successfully been stored in the grain: bigip_f5_trans:{label}'
            .format(trans_id=trans_id, label=label))
    else:
        return data