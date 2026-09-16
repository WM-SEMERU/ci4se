def queues_for_endpoint(event):
    global endpoints
    try:
        ep_name = event['context']['resource-path'].lstrip('/')
        return endpoints[ep_name]['queues']
    except:
        raise Exception('Endpoint not in configuration: /%s' % ep_name)