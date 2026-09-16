def set_namespace_view_settings(self):
    if self.namespacebrowser:
        settings = to_text_string(self.namespacebrowser.get_view_settings())
        code = 'get_ipython().kernel.namespace_view_settings = %s' % settings
        self.silent_execute(code)