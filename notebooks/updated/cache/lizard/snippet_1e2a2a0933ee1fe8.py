def get_first_webview_context(self):
    for context in self.driver_wrapper.driver.contexts:
        if context.startswith('WEBVIEW'):
            return context
    raise Exception('No WEBVIEW context has been found')