def reload_component(self, component):
    dependents = list(reversed(self.list_dependents(component)))
    dependents.append(component)
    for dependent in dependents:
        profile = self.__components[dependent]
        module = __import__(profile.package)
        reload(module)
        object = profile.attribute in dir(module) and getattr(module,
            profile.attribute) or None
        if object and inspect.isclass(object):
            for type in self.__categories.itervalues():
                if type.__name__ in (base.__name__ for base in object.__bases__
                    ):
                    instance = object(name=profile.name)
                    profile.module = module
                    profile.interface = instance
                    LOGGER.info("{0} | '{1}' Component has been reloaded!".
                        format(self.__class__.__name__, profile.name))
    return True