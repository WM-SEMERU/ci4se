def _add_layer_clicked(self):
    layer = self.tree.selectedItems()[0]
    origin = layer.data(0, LAYER_ORIGIN_ROLE)
    if origin == FROM_ANALYSIS['key']:
        parent = layer.data(0, LAYER_PARENT_ANALYSIS_ROLE)
        key = layer.data(0, LAYER_PURPOSE_KEY_OR_ID_ROLE)
        item = QListWidgetItem('%s - %s' % (layer.text(0), parent))
        item.setData(LAYER_PARENT_ANALYSIS_ROLE, parent)
        item.setData(LAYER_PURPOSE_KEY_OR_ID_ROLE, key)
    else:
        item = QListWidgetItem(layer.text(0))
        layer_id = layer.data(0, LAYER_PURPOSE_KEY_OR_ID_ROLE)
        item.setData(LAYER_PURPOSE_KEY_OR_ID_ROLE, layer_id)
    item.setData(LAYER_ORIGIN_ROLE, origin)
    self.list_layers_in_map_report.addItem(item)
    self.tree.invisibleRootItem().removeChild(layer)
    self.tree.clearSelection()