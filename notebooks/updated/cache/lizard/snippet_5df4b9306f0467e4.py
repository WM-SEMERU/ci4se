def compute_wed(self):
    if len(self.cacheConnections) != 0:
        changeConnections = self.cacheConnections
    else:
        changeConnections = self.connections
    for connect in reverse(changeConnections):
        if (connect.active and connect.fromLayer.active and connect.toLayer
            .active):
            connect.wed = connect.wed + Numeric.outerproduct(connect.
                fromLayer.activation, connect.toLayer.delta)
    if len(self.cacheLayers) != 0:
        changeLayers = self.cacheLayers
    else:
        changeLayers = self.layers
    for layer in changeLayers:
        if layer.active:
            layer.wed = layer.wed + layer.delta