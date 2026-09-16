def set_widgets(self):
    last_layer = self.parent.layer and self.parent.layer.id() or None
    self.lblDescribeCanvasAggLayer.clear()
    self.list_compatible_canvas_layers()
    self.auto_select_one_item(self.lstCanvasAggLayers)
    if last_layer:
        layers = []
        for indx in range(self.lstCanvasAggLayers.count()):
            item = self.lstCanvasAggLayers.item(indx)
            layers += [item.data(QtCore.Qt.UserRole)]
        if last_layer in layers:
            self.lstCanvasAggLayers.setCurrentRow(layers.index(last_layer))
    self.lblIconIFCWAggregationFromCanvas.setPixmap(QPixmap(None))