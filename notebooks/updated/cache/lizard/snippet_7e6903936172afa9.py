def send_slack_message(channel, text):
    http = httplib2.Http()
    return http.request(SLACK_MESSAGE_URL, 'POST', body=json.dumps({
        'channel': channel, 'text': text}))