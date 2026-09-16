def get_template(self, template_name, **parameters):
    template_path = pathlib.Path(self.template_dir).joinpath(template_name)
    return get_template(template_path, **parameters)