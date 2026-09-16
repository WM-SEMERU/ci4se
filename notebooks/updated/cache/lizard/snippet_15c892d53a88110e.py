def claim_pep_node(self, node_namespace, *, register_feature=True, notify=False
    ):
    if node_namespace in self._pep_node_claims:
        raise RuntimeError('claiming already claimed node')
    registered_node = RegisteredPEPNode(self, node_namespace,
        register_feature=register_feature, notify=notify)
    finalizer = weakref.finalize(registered_node, weakref.WeakMethod(
        registered_node._unregister))
    finalizer.atexit = False
    self._pep_node_claims[node_namespace] = registered_node
    return registered_node