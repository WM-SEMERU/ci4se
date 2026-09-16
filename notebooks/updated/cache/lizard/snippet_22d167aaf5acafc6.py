def directory(self, query, **kwargs):
    if isinstance(query, dict):
        query = str(query).replace("'", '"')
    return self.__call_api_get('directory', query=query, kwargs=kwargs)