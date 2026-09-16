def load_template(self, templatename, template_string=None):
    if template_string is not None:
        return Template(template_string, **self.tmpl_options)
    if '/' not in templatename:
        templatename = '/' + templatename.replace('.', '/'
            ) + '.' + self.extension
    return self.lookup.get_template(templatename)