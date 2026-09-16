def addSubscribers(self, emails_list):
    if not hasattr(emails_list, '__iter__'):
        error_msg = "Input parameter 'emails_list' is not iterable"
        self.log.error(error_msg)
        raise exception.BadValue(error_msg)
    existed_flags = False
    headers, raw_data = self._perform_subscribe()
    for email in emails_list:
        existed_flag, raw_data = self._add_subscriber(email, raw_data)
        existed_flags = existed_flags and existed_flag
    if existed_flags:
        return
    self._update_subscribe(headers, raw_data)
    self.log.info('Successfully add subscribers: %s for <Workitem %s>',
        emails_list, self)