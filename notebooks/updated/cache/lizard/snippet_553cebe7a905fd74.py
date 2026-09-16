def rpc_reply(channel, original_headers, message, properties=None):
    if not properties:
        properties = {}
    properties['correlation_id'] = original_headers.correlation_id
    publish_message(channel, '', original_headers.reply_to, message, properties
        )