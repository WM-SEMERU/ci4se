def _assign_work_unit(self, node):
    assert self.workqueue
    scope, work_unit = self.workqueue.popitem(last=False)
    assigned_to_node = self.assigned_work.setdefault(node, default=
        OrderedDict())
    assigned_to_node[scope] = work_unit
    worker_collection = self.registered_collections[node]
    nodeids_indexes = [worker_collection.index(nodeid) for nodeid,
        completed in work_unit.items() if not completed]
    node.send_runtest_some(nodeids_indexes)