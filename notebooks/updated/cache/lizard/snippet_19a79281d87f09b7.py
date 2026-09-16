def create_install_template_skin(self):
    ckan_extension_template(self.name, self.target)
    self.install_package_develop('ckanext-' + self.name + 'theme')