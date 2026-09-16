def delete(self, service_name, *ids, **kwargs):
    return self._send(requests.delete, service_name, id=ids, **kwargs)