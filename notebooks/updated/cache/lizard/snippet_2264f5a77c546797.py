def _as_json(self, response):
    content = response.text() if hasattr(response, 'body') else response.text
    try:
        return json.loads(content)
    except ValueError:
        raise DeserializationError(
            'Error occurred in deserializing the response body.')