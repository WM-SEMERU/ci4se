def store_item(self, item):
    assert not isinstance(item, RamGraphDBNode)
    item_hash = graph_hash(item)
    if item_hash not in self.nodes:
        self.nodes[item_hash] = RamGraphDBNode(item)
    return self.nodes[item_hash]