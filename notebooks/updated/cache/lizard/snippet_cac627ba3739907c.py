def find_contexts(self, in_request=None, in_resolve=None):
    names = self.context_names
    if in_request:

        def _in_request(name):
            context = self.context(name)
            packages = set(x.name for x in context.requested_packages(True))
            return in_request in packages
        names = [x for x in names if _in_request(x)]
    if in_resolve:
        if isinstance(in_resolve, basestring):
            in_resolve = PackageRequest(in_resolve)

        def _in_resolve(name):
            context = self.context(name)
            variant = context.get_resolved_package(in_resolve.name)
            if variant:
                overlap = variant.version in in_resolve.range
                return (in_resolve.conflict and not overlap or overlap and 
                    not in_resolve.conflict)
            else:
                return in_resolve.conflict
        names = [x for x in names if _in_resolve(x)]
    return names