def default_change_form_template(self):
    opts = self.model._meta
    app_label = opts.app_label
    return select_template_name(('admin/{0}/{1}/change_form.html'.format(
        app_label, opts.object_name.lower()), 'admin/{0}/change_form.html'.
        format(app_label), 'admin/change_form.html'))