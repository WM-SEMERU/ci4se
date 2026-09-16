def get_template_names(self):
    if self.request.is_ajax():
        return [self.list_template_name]
    else:
        return super(Search, self).get_template_names()