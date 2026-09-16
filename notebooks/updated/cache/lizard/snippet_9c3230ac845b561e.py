def query_rates(self, pairs=[]):
    payload = {'id': self._session}
    if pairs:
        payload['c'] = _clean_pairs(pairs)
    response = requests.get(self._api_url, params=payload)
    mapped_data = _fx_mapping(response.content.split('\n')[:-2])
    return Series(mapped_data) if len(mapped_data) == 1 else DataFrame(
        mapped_data)