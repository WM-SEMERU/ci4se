def send_msg_to_webhook(self, json_payload, log_msg):
    if SILENCE_OVERRIDE:
        return
    payload = {'text': log_msg, 'attachments': [json_payload]}
    header = {'Content-Type': 'application/json'}
    try:
        request = requests.post(self.webhook_url, headers=header, json=payload)
        request.raise_for_status()
    except Exception as error_msg:
        warning_msg = ('EXCEPTION: UNABLE TO COMMIT LOG MESSAGE' +
            '\n\texception={0}'.format(repr(error_msg)) + '\n\tmessage={0}'
            .format(log_msg))
        warnings.warn(warning_msg, exceptions.WebhookFailedEmitWarning)