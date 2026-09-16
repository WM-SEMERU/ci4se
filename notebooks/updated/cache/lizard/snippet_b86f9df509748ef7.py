def create_message(username, message):
    message = message.replace('\n', '<br/>')
    return (
        '{{"service":1, "data":{{"message":"{mes}", "username":"{user}"}} }}'
        .format(mes=message, user=username))