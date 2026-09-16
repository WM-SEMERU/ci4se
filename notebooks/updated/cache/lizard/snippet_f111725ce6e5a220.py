def list(self, resource):
    return self.service.list(resource, self.url_prefix, self.auth, self.
        session, self.session_send_opts)