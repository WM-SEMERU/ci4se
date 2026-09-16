def unregister_controllers(self):
    for name, module in self._controller_modules.items():
        logging.debug('Destroying %s.', name)
        with expects.expect_no_raises('Exception occurred destroying %s.' %
            name):
            module.destroy(self._controller_objects[name])
    self._controller_objects = collections.OrderedDict()
    self._controller_modules = {}