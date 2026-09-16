def deroot(self, label='OLDROOT'):
    if self.root.edge_length is not None:
        self.root.add_child(Node(edge_length=self.root.edge_length, label=
            label))
        self.root.edge_length = None