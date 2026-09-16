def add_unique_template_variables(self, options):
    options.update(dict(image=self.image, coordinates=self.coordinates))