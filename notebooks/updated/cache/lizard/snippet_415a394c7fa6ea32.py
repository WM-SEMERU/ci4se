def threw(self, error_type=None):
    if not error_type:
        return True if len(self.exceptions) > 0 else False
    else:
        return uch.obj_in_list(self.exceptions, error_type)