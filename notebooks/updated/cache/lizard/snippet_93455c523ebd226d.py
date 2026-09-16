def open_recruitment(self, n=1):
    logger.info('Opening HotAir recruitment for {} participants'.format(n))
    recruitments = self.recruit(n)
    message = 'Recruitment requests will open browser windows automatically.'
    return {'items': recruitments, 'message': message}