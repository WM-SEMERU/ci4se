def post_partitioned(self, endpoint, json, params=None, thresh=1000):
    if not isinstance(json, dict):
        raise ClientException('Parameter `json` must be a dict')
    if not isinstance(thresh, int) or thresh < 2:
        raise ClientException('`thresh` must be integer of 2 or larger')
    try:
        key = next(iter(json))
    except StopIteration:
        raise ClientException('`json` is empty')
    else:
        if len(json.keys()) != 1:
            raise ClientException(
                'Must submit exactly one key in payload - e.g. json={"dataElements": [...]"}'
                )
        if not json.get(key):
            raise ClientException("payload for key '{}' is empty".format(key))
        else:
            for data in partition_payload(data=json, key=key, thresh=thresh):
                yield self.post(endpoint, json=data, params=params)