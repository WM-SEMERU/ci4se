def _process_block(self, node, **kwargs):
    if not hasattr(node, 'super_block'):
        node.super_block = None
        child_block = self.child_blocks.get(node.name)
        if child_block:
            last_block = child_block
            while hasattr(last_block, 'super_block'):
                last_block = child_block.super_block
            last_block.super_block = node
            node = child_block
    for n in node.body:
        self._process_node(n, super_block=node.super_block, **kwargs)