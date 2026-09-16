def recruit(self, n=1):
    logger.info('Recruiting {} CLI participants'.format(n))
    urls = []
    template = (
        '{}/ad?recruiter={}&assignmentId={}&hitId={}&workerId={}&mode={}')
    for i in range(n):
        ad_url = template.format(get_base_url(), self.nickname,
            generate_random_id(), generate_random_id(), generate_random_id(
            ), self._get_mode())
        logger.info('{} {}'.format(NEW_RECRUIT_LOG_PREFIX, ad_url))
        urls.append(ad_url)
    return urls