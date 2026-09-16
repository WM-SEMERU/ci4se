def interact(self, ctx, location, ir_err):
    p = ir_err.interaction_method(self.kind(), WebBrowserInteractionInfo)
    if not location.endswith('/'):
        location += '/'
    visit_url = urljoin(location, p.visit_url)
    wait_token_url = urljoin(location, p.wait_token_url)
    self._open_web_browser(visit_url)
    return self._wait_for_token(ctx, wait_token_url)