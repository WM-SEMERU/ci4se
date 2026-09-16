def get_bounding_box(self, resource, resolution, id, bb_type='loose'):
    return self.service.get_bounding_box(resource, resolution, id, bb_type,
        self.url_prefix, self.auth, self.session, self.session_send_opts)