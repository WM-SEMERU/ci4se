def closest(self, obj, group, defaults=True):
    components = obj.__class__.__name__, group_sanitizer(obj.group
        ), label_sanitizer(obj.label)
    target = '.'.join([c for c in components if c])
    return self.find(components).options(group, target=target, defaults=
        defaults)