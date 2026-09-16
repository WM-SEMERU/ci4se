def close(self):
    from neobolt.exceptions import CypherError
    self._assert_open()
    try:
        self.sync()
    except CypherError:
        self.success = False
        raise
    finally:
        if self.session.has_transaction():
            if self.success:
                self.session.commit_transaction()
            else:
                self.session.rollback_transaction()
        self._closed = True
        self.on_close()