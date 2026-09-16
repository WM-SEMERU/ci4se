def set_base_url(self, platform: str='prod'):
    platform = platform.lower()
    self.platform = platform
    if platform == 'prod':
        ssl = True
        logging.debug('Using production platform.')
    elif platform == 'qa':
        ssl = False
        logging.debug('Using Quality Assurance platform (reduced perfs).')
    else:
        logging.error('Platform must be one of: {}'.format(' | '.join(self.
            API_URLS.keys())))
        raise ValueError(3, 'Platform must be one of: {}'.format(' | '.join
            (self.API_URLS.keys())))
    return platform.lower(), self.API_URLS.get(platform), self.APP_URLS.get(
        platform), self.CSW_URLS.get(platform), self.MNG_URLS.get(platform
        ), self.OC_URLS.get(platform), ssl