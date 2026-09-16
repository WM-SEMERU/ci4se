def deliver_hook(instance, target, payload_override=None):
    payload = payload_override or serialize_hook(instance)
    if hasattr(settings, 'HOOK_DELIVERER'):
        deliverer = get_module(settings.HOOK_DELIVERER)
        deliverer(target, payload, instance=instance)
    else:
        client.post(url=target, data=json.dumps(payload, cls=serializers.
            json.DjangoJSONEncoder), headers={'Content-Type':
            'application/json'})
    return None