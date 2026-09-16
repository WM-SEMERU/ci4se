def post_message(consumers, lti_key, url, body):
    content_type = 'application/xml'
    method = 'POST'
    _, content = _post_patched_request(consumers, lti_key, body, url,
        method, content_type)
    is_success = b'<imsx_codeMajor>success</imsx_codeMajor>' in content
    log.debug('is success %s', is_success)
    return is_success