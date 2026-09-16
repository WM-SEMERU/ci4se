def discover(self, ip):
    if self.verbose > 0:
        print(
            """Discovery codes:
    . depth             %s connection error
    %s discovering node  %s numerating adjacencies
    %s include node      %s leaf node
"""
             % (DCODE_ERR_SNMP_STR, DCODE_DISCOVERED_STR,
            DCODE_STEP_INTO_STR, DCODE_INCLUDE_STR, DCODE_LEAF_STR))
        print('Discovering network...')
    node, new_node = self.__query_node(ip, 'UNKNOWN')
    self.root_node = node
    if node != None:
        self.nodes.append(node)
        self.__print_step(node.ip[0], node.name, 0, DCODE_ROOT |
            DCODE_DISCOVERED)
        self.__discover_node(node, 0)
    else:
        return
    for n in self.nodes:
        if (n.serial == None) | (n.plat == None) | (n.ios == None):
            n.opts.get_chassis_info = True
            if n.serial == None:
                n.opts.get_serial = True
            if n.ios == None:
                n.opts.get_ios = True
            if n.plat == None:
                n.opts.get_plat = True
            n.query_node()