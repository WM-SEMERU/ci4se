def slack_notify(self):
    utils.banner('Sending slack notification')
    if self.env.startswith('prod'):
        notify = slacknotify.SlackNotification(app=self.app, env=self.env,
            prop_path=self.json_path)
        notify.post_message()
    else:
        LOG.info('No slack message sent, not production environment')