def sanitize_http_request_body(client, event):
    try:
        body = force_text(event['context']['request']['body'], errors='replace'
            )
    except (KeyError, TypeError):
        return event
    if '=' in body:
        sanitized_query_string = _sanitize_string(body, '&', '=')
        event['context']['request']['body'] = sanitized_query_string
    return event