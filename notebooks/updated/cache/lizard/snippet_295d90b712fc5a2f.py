def get_config(self, service, setting):
    try:
        return self.get_service(service)[setting]
    except KeyError:
        return getattr(self, setting + '_DEFAULT')