def create_new_reference(self, obj, global_ref=False):
    opaque_ref = self.state.project.loader.extern_object.allocate()
    l.debug('Map %s to opaque reference 0x%x', obj, opaque_ref)
    if global_ref:
        self.global_refs[opaque_ref] = obj
    else:
        self.local_refs[opaque_ref] = obj
    return opaque_ref