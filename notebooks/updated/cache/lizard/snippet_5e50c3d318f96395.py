def add_layer_item(self, layer):
    if not layer.is_draft_version:
        raise ValueError("Layer isn't a draft version")
    self.items.append(layer.latest_version)