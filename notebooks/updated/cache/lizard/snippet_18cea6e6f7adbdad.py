def _unregister_all_factories(self):
    factories = list(self.__factories.keys())
    for factory_name in factories:
        self.unregister_factory(factory_name)