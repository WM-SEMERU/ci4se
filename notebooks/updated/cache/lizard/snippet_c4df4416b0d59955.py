def parse_value_refarray(self, tup_tree):
    self.check_node(tup_tree, 'VALUE.REFARRAY')
    children = self.list_of_various(tup_tree, ('VALUE.REFERENCE', 'VALUE.NULL')
        )
    return children