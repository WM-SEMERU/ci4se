def init_reddit(generator):
    auth_dict = generator.settings.get('REDDIT_POSTER_AUTH')
    if auth_dict is None:
        log.info(
            "Could not find REDDIT_POSTER_AUTH key in settings, reddit plugin won't function"
            )
        generator.get_reddit = lambda : None
        return
    reddit = praw.Reddit(**auth_dict)
    generator.get_reddit = lambda : reddit