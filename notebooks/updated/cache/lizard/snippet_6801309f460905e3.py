def wants(cls, *service_names):

    def _decorator(cls_):
        for service_name in service_names:
            cls_._services_requested[service_name] = 'want'
        return cls_
    return _decorator