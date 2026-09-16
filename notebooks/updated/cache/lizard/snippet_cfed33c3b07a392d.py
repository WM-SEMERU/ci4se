def gen_body(self):
    for treepos in sorted(self.treepositions):
        node = self.dgtree[treepos]
        node_id = self.get_node_id(treepos)
        node_type = get_node_type(node)
        if node_type in (TreeNodeTypes.leaf_node, TreeNodeTypes.relation_node):
            relname, parent_id = self.get_relname_and_parent(treepos)
            attrib_list = [('id', node_id)]
            if parent_id is not None:
                attrib_list.extend([('parent', parent_id), ('relname',
                    relname)])
            if node_type == TreeNodeTypes.leaf_node:
                self.body['segments'].append(E('segment', node, OrderedDict
                    (attrib_list)))
            else:
                group_type = self.get_group_type(treepos)
                attrib_list.insert(1, ('type', group_type))
                self.body['groups'].append(E('group', OrderedDict(attrib_list))
                    )