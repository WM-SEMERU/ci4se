def save_data(self, trigger_id, **data):
    status = False
    data['output_format'] = 'md'
    title, content = super(ServiceReddit, self).save_data(trigger_id, **data)
    if self.token:
        trigger = Reddit.objects.get(trigger_id=trigger_id)
        if trigger.share_link:
            status = self.reddit.subreddit(trigger.subreddit).submit(title=
                title, url=content)
        else:
            status = self.reddit.subreddit(trigger.subreddit).submit(title=
                title, selftext=content)
        sentence = str('reddit submission {} created').format(title)
        logger.debug(sentence)
    else:
        msg = 'no token or link provided for trigger ID {} '.format(trigger_id)
        logger.critical(msg)
        update_result(trigger_id, msg=msg, status=False)
    return status