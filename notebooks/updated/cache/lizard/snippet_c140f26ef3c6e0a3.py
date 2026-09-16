def exclude_from_all(self, exclude_regex):
    try:
        re.compile(exclude_regex)
    except re.error:
        raise ZAPError('Invalid regex "{0}" provided'.format(exclude_regex))
    self.logger.debug('Excluding {0} from proxy, spider and active scanner.'
        .format(exclude_regex))
    self.zap.core.exclude_from_proxy(exclude_regex)
    self.zap.spider.exclude_from_scan(exclude_regex)
    self.zap.ascan.exclude_from_scan(exclude_regex)