def _concrete_instance_list(self, instance_docs):
    if not instance_docs:
        return []
    return list(filter(None, [self._concrete_instance(instance_doc=doc) for
        doc in instance_docs]))