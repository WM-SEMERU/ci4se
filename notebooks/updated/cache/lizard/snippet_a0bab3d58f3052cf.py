def stats(self):
    return self._client.get('{}/stats'.format(Instance.api_endpoint), model
        =self)