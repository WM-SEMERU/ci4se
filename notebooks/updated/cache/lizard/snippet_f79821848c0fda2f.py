def available(self):
    url = api.get_url(self.context)
    if self.context == api.get_portal():
        return True
    if url.endswith('/front-page'):
        return True
    if url.endswith('/manage_results'):
        return True
    return False