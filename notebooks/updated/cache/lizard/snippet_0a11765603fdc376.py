def full_post_process(self, conn_method_name, result):
    result = self.post_process(conn_method_name, result)
    custom_method_name = 'post_process_{0}'.format(conn_method_name)
    custom_method = getattr(self, custom_method_name, None)
    if custom_method:
        result = custom_method(result)
    return result