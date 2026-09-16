def _get_template(self, template_name, template_file):
    template = os.path.join(self.location, 'templates', template_name,
        template_file)
    return jinja2.Template(open(template).read())