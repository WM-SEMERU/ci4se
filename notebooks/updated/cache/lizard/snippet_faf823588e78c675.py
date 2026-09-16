def _to_tree(self, rule_node):
    orig_rule = self.orig_rules[rule_node.rule.alias]
    children = []
    for child in rule_node.children:
        if isinstance(child, RuleNode):
            children.append(self._to_tree(child))
        else:
            assert isinstance(child.name, Token)
            children.append(child.name)
    t = Tree(orig_rule.origin, children)
    t.rule = orig_rule
    return t