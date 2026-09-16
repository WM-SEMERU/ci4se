def add_brok(self, brok, broker_uuid=None):
    brok.instance_id = self.instance_id
    if brok.type == 'monitoring_log':
        with self.my_daemon.events_lock:
            self.my_daemon.events.append(brok)
        statsmgr.counter('events', 1)
        return
    if broker_uuid:
        if broker_uuid not in self.my_daemon.brokers:
            logger.info('Unknown broker: %s / %s!', broker_uuid, self.
                my_daemon.brokers)
            return
        broker_link = self.my_daemon.brokers[broker_uuid]
        logger.debug('Adding a brok %s for: %s', brok.type, broker_uuid)
        self.my_daemon.brokers[broker_link.uuid].broks.append(brok)
        self.nb_broks += 1
    else:
        logger.debug('Adding a brok %s to all brokers', brok.type)
        for broker_link_uuid in self.my_daemon.brokers:
            logger.debug('- adding to %s', self.my_daemon.brokers[
                broker_link_uuid])
            self.my_daemon.brokers[broker_link_uuid].broks.append(brok)
            self.nb_broks += 1