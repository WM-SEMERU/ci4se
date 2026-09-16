def get_default_prefix(self, instance=None):
    if instance is None and hasattr(self, 'instance'):
        instance = self.instance
    if instance and instance.id is not None:
        instance_prefix = self.default_instance_prefix
        if instance_prefix is None:
            instance_prefix = self.__class__.__name__.lower() + 'i-'
        return '{0}{1}'.format(instance_prefix, instance.id)
    if self.default_new_prefix is not None:
        return self.default_new_prefix
    return self.__class__.__name__.lower() + 'new-'