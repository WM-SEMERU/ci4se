def manage_finished_checks(self, queue):
    to_del = []
    wait_time = 1.0
    now = time.time()
    logger.debug('--- manage finished checks')
    for action in self.checks:
        logger.debug(
            '--- checking: last poll: %s, now: %s, wait_time: %s, action: %s',
            action.last_poll, now, action.wait_time, action)
        if (action.status == ACT_STATUS_LAUNCHED and action.last_poll < now -
            action.wait_time):
            action.check_finished(self.max_plugins_output_length)
            wait_time = min(wait_time, action.wait_time)
        if action.status in [ACT_STATUS_DONE, ACT_STATUS_TIMEOUT]:
            logger.debug('--- check done/timeout: %s', action.uuid)
            self.actions_finished += 1
            to_del.append(action)
            try:
                msg = Message(_type='Done', data=action, source=self._id)
                logger.debug('Queuing message: %s', msg)
                queue.put_nowait(msg)
            except Exception as exp:
                logger.error('Failed putting messages in returns queue: %s',
                    str(exp))
    for chk in to_del:
        logger.debug('--- delete check: %s', chk.uuid)
        self.checks.remove(chk)
    logger.debug('--- manage finished checks terminated, I will wait: %s',
        wait_time)
    time.sleep(wait_time)