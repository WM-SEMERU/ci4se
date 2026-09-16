def _expand_url(short_link, subreddit=None):
    message_scheme = 'https://reddit.com/message/messages/{}'
    comment_scheme = 'https://reddit.com/r/{}/comments/{}/-/{}'
    post_scheme = 'https://reddit.com/r/{}/comments/{}/'
    if short_link == '':
        return None
    else:
        parts = short_link.split(',')
        if parts[0] == 'm':
            return message_scheme.format(parts[1])
        if parts[0] == 'l' and subreddit:
            if len(parts) > 2:
                return comment_scheme.format(subreddit, parts[1], parts[2])
            else:
                return post_scheme.format(subreddit, parts[1])
        elif not subreddit:
            raise ValueError('Subreddit name must be provided')
        else:
            return None