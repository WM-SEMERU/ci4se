def load_template(self, name):
    if name in self.cached_templates:
        logger.debug('Using cached template: %s', name)
        return self.cached_templates[name]
    logger.debug('Attempting to find template by name: %s', name)
    name_with_ext, provider_name, base_path = self.find_template_details(name)
    full_path = None
    if base_path is not None:
        full_path = os.path.join(base_path, name_with_ext)
    template = template_exception_handler(lambda : self.get_provider(
        provider_name).load_template(name_with_ext, full_path=full_path),
        self.error_context, filename=full_path)
    self.cached_templates[name] = template
    return template