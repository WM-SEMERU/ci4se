def get_api_service(self, name=None):
    try:
        svc = self.services_by_name.get(name, None)
        if svc is None:
            raise ValueError(f"Couldn't find the API service configuration")
        return svc
    except:
        raise Exception(f'Failed to retrieve the API service configuration')