def do_transaction(self, function, *args, **kwargs):
    for wait_in_seconds in self.backoff_generator():
        try:
            with self.config.db_transaction() as trans:
                function(trans, *args, **kwargs)
                trans.commit()
                break
        except self.config.db_transaction.operational_exceptions:
            pass
        print('failure in transaction - retry in %s seconds' % wait_in_seconds)
        self.responsive_sleep(wait_in_seconds,
            'waiting for retry after failure in transaction')