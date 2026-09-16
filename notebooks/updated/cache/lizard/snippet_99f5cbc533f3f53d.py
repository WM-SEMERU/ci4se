def send_change_notification(hub, topic_url, updated_content=None):
    if updated_content:
        body = base64.b64decode(updated_content['content'])
    else:
        body, updated_content = get_new_content(hub.config, topic_url)
    b64_body = updated_content['content']
    headers = updated_content['headers']
    link_header = headers.get('Link', '')
    if 'rel="hub"' not in link_header or 'rel="self"' not in link_header:
        raise NotificationError(INVALID_LINK)
    for callback_url, secret in hub.storage.get_callbacks(topic_url):
        schedule_request(hub, topic_url, callback_url, secret, body,
            b64_body, headers)