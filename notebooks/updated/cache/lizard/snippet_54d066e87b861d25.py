def check_cache(self, e_tag, match):
    if e_tag != match:
        return False
    self.send_response(304)
    self.send_header('ETag', e_tag)
    self.send_header('Cache-Control', 'max-age={0}'.format(self.server.max_age)
        )
    self.end_headers()
    thread_local.size = 0
    return True