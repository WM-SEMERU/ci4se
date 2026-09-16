def _decode_response(response):
    content = response.content.strip()
    logging.debug(content[:512])
    response.raise_for_status()
    if content.startswith(GERRIT_MAGIC_JSON_PREFIX):
        content = content[len(GERRIT_MAGIC_JSON_PREFIX):]
    try:
        return json.loads(content)
    except ValueError:
        logging.error('Invalid json content: %s' % content)
        raise