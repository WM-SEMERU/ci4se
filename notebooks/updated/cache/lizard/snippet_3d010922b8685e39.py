def start_transport(transport, username, key):
    transport.start_client()
    agent = paramiko.agent.Agent()
    keys = itertools.chain((key,) if key else (), agent.get_keys())
    for test_key in keys:
        try:
            transport.auth_publickey(username, test_key)
            break
        except paramiko.AuthenticationException as e:
            pass
    else:
        raise ValueError('No valid key supplied')
    return transport