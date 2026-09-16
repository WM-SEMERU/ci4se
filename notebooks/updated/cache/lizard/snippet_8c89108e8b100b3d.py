def do_tree(self, params):
    self.show_output('.')
    for child, level in self._zk.tree(params.path, params.max_depth):
        self.show_output('%s├── %s', '│   ' * level, child)