def _return_assoc_class_tuples(self, rtn_classnames, namespace, iq, ico, pl):
    rtn_tups = []
    for cn in rtn_classnames:
        rtn_tups.append((CIMClassName(cn, namespace=namespace, host=self.
            host), self._get_class(cn, namespace=namespace,
            include_qualifiers=iq, include_classorigin=ico, property_list=pl)))
    return self._return_assoc_tuple(rtn_tups)