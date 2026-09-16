def print_javascript_error(self):
    errors = self.get_javascript_error(return_type='list')
    if errors:
        self.info_log('Javascript error:')
        for error in errors:
            self.info_log(error)