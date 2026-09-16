def parse_host(self, tup_tree):
    self.check_node(tup_tree, 'HOST', (), (), (), allow_pcdata=True)
    return self.pcdata(tup_tree)