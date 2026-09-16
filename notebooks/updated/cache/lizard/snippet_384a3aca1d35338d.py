def ports(self):

    def has_port(node, args):
        if node.get_port_by_ref(args):
            return node
        return None
    with self._mutex:
        if not self._ports:
            self._ports = []
            for p in self._obj.ports:
                if self.owner and self.owner.owner:
                    root = self.owner.owner.root
                    owner_nodes = [n for n in root.iterate(has_port, args=p,
                        filter=['is_component']) if n]
                    if not owner_nodes:
                        self._ports.append(('Unknown', None))
                    else:
                        port_owner = owner_nodes[0]
                        port_owner_path = port_owner.full_path_str
                        port_name = p.get_port_profile().name
                        prefix = port_owner.instance_name + '.'
                        if port_name.startswith(prefix):
                            port_name = port_name[len(prefix):]
                        self._ports.append((port_owner_path + ':' +
                            port_name, parse_port(p, self.owner.owner)))
                else:
                    self._ports.append((p.get_port_profile().name,
                        parse_port(p, None)))
    return self._ports