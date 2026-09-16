def open_recruitment(self, n=1):
    logger.info('Opening Bot recruitment for {} participants'.format(n))
    factory = self._get_bot_factory()
    bot_class_name = factory('', '', '').__class__.__name__
    return {'items': self.recruit(n), 'message':
        'Bot recruitment started using {}'.format(bot_class_name)}