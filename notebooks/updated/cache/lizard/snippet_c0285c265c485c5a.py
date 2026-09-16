def _on_github_request(self, future, response):
    try:
        content = escape.json_decode(response.body)
    except ValueError as error:
        future.set_exception(Exception('Github error: %s' % response.body))
        return
    if 'error' in content:
        future.set_exception(Exception('Github error: %s' % str(content[
            'error'])))
        return
    future.set_result(content)