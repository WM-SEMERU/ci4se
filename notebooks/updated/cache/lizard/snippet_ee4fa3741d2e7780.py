def get_versioned_references_for(self, instance):
    vrefs = []
    refs = instance.getRefs(relationship=self.relationship)
    ref_versions = getattr(instance, REFERENCE_VERSIONS, None)
    if ref_versions is None:
        return refs
    for ref in refs:
        uid = api.get_uid(ref)
        version = ref_versions.get(uid)
        vrefs.append(self.retrieve_version(ref, version))
    return vrefs