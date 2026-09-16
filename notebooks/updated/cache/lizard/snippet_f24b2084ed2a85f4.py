def poll_all_received_events(self):
    locked = False
    try:
        with Timeout(10):
            locked = self.lock.acquire(blocking=False)
            if not locked:
                return
            else:
                received_transfers = (self.api.
                    get_raiden_events_payment_history(token_address=self.
                    token_address, offset=self.last_poll_offset))
                received_transfers = [event for event in received_transfers if
                    type(event) == EventPaymentReceivedSuccess]
                for event in received_transfers:
                    transfer = copy.deepcopy(event)
                    self.received_transfers.put(transfer)
                if received_transfers:
                    self.last_poll_offset += len(received_transfers)
                if not self.echo_worker_greenlet.started:
                    log.debug('restarting echo_worker_greenlet', dead=self.
                        echo_worker_greenlet.dead, successful=self.
                        echo_worker_greenlet.successful(), exception=self.
                        echo_worker_greenlet.exception)
                    self.echo_worker_greenlet = gevent.spawn(self.echo_worker)
    except Timeout:
        log.info('timeout while polling for events')
    finally:
        if locked:
            self.lock.release()