def clear_instances(self, instances=None):
    if instances is None:
        instances = self.instances[:]
    for instance in instances:
        self.remove_instance(instance)