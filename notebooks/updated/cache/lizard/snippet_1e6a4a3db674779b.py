def get(self, instance_name):
    url = self._url + instance_name + '/'
    response = requests.get(url, **self._default_request_kwargs)
    data = self._get_response_data(response)
    return self._concrete_instance(data)