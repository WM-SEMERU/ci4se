def disqus_recent_comments(context, shortname='', num_items=5,
    excerpt_length=200, hide_avatars=0, avatar_size=32):
    shortname = getattr(settings, 'DISQUS_WEBSITE_SHORTNAME', shortname)
    return {'shortname': shortname, 'num_items': num_items, 'hide_avatars':
        hide_avatars, 'avatar_size': avatar_size, 'excerpt_length':
        excerpt_length, 'config': get_config(context)}