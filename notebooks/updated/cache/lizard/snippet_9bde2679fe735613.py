def print_nodes(self, order='in', priority='L', display=None, root=None):
    old_display = None
    if root == None:
        root = self.root.name
    if display == None:
        display = self.attr['display']
    else:
        old_display = self.attr['display']
        self.attr['display'] = display
    if priority == 'L':
        first_child = self.get_left_child
        second_child = self.get_right_child
    else:
        first_child = self.get_right_child
        second_child = self.get_left_child
    if order == 'pre':
        print(root)
    if first_child(root) is not None:
        if display:
            self.display(highlight=[root])
        self.print_nodes(order, priority, display, first_child(root))
    if order == 'in':
        print(root)
    if second_child(root) is not None:
        if display:
            self.display(highlight=[root])
        self.print_nodes(order, priority, display, second_child(root))
    if order == 'post':
        print(root)
    if display:
        self.display(highlight=[root])
    if old_display:
        self.attr['display'] = old_display