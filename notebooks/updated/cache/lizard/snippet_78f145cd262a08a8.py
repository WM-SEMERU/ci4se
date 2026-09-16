def post_slack_message(message=None, channel=None, username=None,
    icon_emoji=None):
    LOG.debug('Slack Channel: %s\nSlack Message: %s', channel, message)
    slack = slacker.Slacker(SLACK_TOKEN)
    try:
        slack.chat.post_message(channel=channel, text=message, username=
            username, icon_emoji=icon_emoji)
        LOG.info('Message posted to %s', channel)
    except slacker.Error:
        LOG.info('error posted message to %s', channel)