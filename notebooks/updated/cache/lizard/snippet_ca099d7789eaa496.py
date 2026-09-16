def delete_bigger(self):
    logger.info('Deleting all mails strictly bigger than {} bytes...'.
        format(self.smallest_size))
    candidates = [mail for mail in self.pool if mail.size > self.smallest_size]
    if len(candidates) == self.size:
        logger.warning('Skip deletion: all {} mails share the same size.'.
            format(self.size))
    logger.info('{} candidates found for deletion.'.format(len(candidates)))
    for mail in candidates:
        self.delete(mail)