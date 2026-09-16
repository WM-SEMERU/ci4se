def do_rm(self, params):
    for path in params.paths:
        try:
            self.client_context.delete(path)
        except NotEmptyError:
            self.show_output('%s is not empty.', path)
        except NoNodeError:
            self.show_output("%s doesn't exist.", path)