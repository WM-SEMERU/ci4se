def do_check(self, params):
    if not self.in_transaction:
        return
    self.client_context.check(params.path, params.version)