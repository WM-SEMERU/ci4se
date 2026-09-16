def add_node(self, node):
    new = ClusterNode.from_uri(node['addr'])
    cluster_member = self.nodes[0]
    check_new_nodes([new], [cluster_member])
    new.meet(cluster_member.host, cluster_member.port)
    self.nodes.append(new)
    self.wait()
    if node['role'] != 'slave':
        return
    if 'master' in node:
        target = self.get_node(node['master'])
        if not target:
            raise NodeNotFound(node['master'])
    else:
        masters = sorted(self.masters, key=lambda x: len(x.slaves(x.name)))
        target = masters[0]
    new.replicate(target.name)
    new.flush_cache()
    target.flush_cache()