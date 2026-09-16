def generate_form_data(self, **kwargs):
    self.children = add_missing_children(self.contained_children, self.children
        )
    kwargs['children'] = self.children
    return FormGenerator(**kwargs)