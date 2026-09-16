def remove_attribution_layer(self):
    if self.attribution_layer is not None:
        this_node = self.attribution_layer.get_node()
        self.root.remove(this_node)
        self.attribution_layer = None
    if self.header is not None:
        self.header.remove_lp('attribution')