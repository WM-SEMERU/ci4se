def send(sender_instance):
    m = Mailin('https://api.sendinblue.com/v2.0', sender_instance._kwargs.
        get('api_key'))
    data = {'to': email_list_to_email_dict(sender_instance._recipient_list),
        'cc': email_list_to_email_dict(sender_instance._cc), 'bcc':
        email_list_to_email_dict(sender_instance._bcc), 'from':
        email_address_to_list(sender_instance._from_email), 'subject':
        sender_instance._subject}
    if sender_instance._template.is_html:
        data.update({'html': sender_instance._message, 'headers': {
            'Content-Type': 'text/html; charset=utf-8'}})
    else:
        data.update({'text': sender_instance._message})
    if 'attachments' in sender_instance._kwargs:
        data['attachment'] = {}
        for attachment in sender_instance._kwargs['attachments']:
            data['attachment'][attachment[0]] = base64.b64encode(attachment[1])
    result = m.send_email(data)
    if result['code'] != 'success':
        raise SendInBlueError(result['message'])