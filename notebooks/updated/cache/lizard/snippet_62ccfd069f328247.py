def instances_set(self, root, reservation):
    instances = []
    for instance_data in root.find('instancesSet'):
        instances.append(self.instance(instance_data, reservation))
    return instances