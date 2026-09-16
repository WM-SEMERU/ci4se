def policy_create(request, **kwargs):
    body = {'policy': kwargs}
    policy = neutronclient(request).create_qos_policy(body=body).get('policy')
    return QoSPolicy(policy)