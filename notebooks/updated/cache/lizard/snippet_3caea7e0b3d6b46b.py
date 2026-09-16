def print_email(message, app):
    invenio_mail = app.extensions['invenio-mail']
    with invenio_mail._lock:
        invenio_mail.stream.write('{0}\n{1}\n'.format(message.as_string(), 
            '-' * 79))
        invenio_mail.stream.flush()