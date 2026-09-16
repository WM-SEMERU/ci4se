def send_mass_mail(data_tuple, fail_silently=False, auth_user=None,
    auth_password=None, connection=None):
    connection = connection or get_connection(username=auth_user, password=
        auth_password, fail_silently=fail_silently)
    messages = [EmailMessage(subject, message, sender, recipient) for 
        subject, message, sender, recipient in data_tuple]
    return connection.send_messages(messages)