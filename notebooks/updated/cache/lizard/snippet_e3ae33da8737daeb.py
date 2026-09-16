def remove_text_layer(self):
    if self.text_layer is not None:
        this_node = self.text_layer.get_node()
        self.root.remove(this_node)
        self.text_layer = None
    if self.header is not None:
        self.header.remove_lp('text')