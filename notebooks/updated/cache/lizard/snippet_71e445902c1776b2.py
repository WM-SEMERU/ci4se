def prop_from(self, startLayers):
    if self.verbosity > 2:
        print('Partially propagating network:')
    propagateLayers = []
    for startLayer in startLayers:
        for layer in self.layers:
            if self.path(startLayer, layer):
                propagateLayers.append(layer)
    for layer in propagateLayers:
        if layer.active:
            layer.netinput = layer.weight.copy()
    for layer in propagateLayers:
        if layer.active:
            for connection in self.connections:
                if connection.active and connection.toLayer.name == layer.name:
                    connection.toLayer.netinput = (connection.toLayer.
                        netinput + Numeric.matrixmultiply(connection.
                        fromLayer.activation, connection.weight))
            if layer.type != 'Input':
                layer.activation = self.activationFunction(layer.netinput)
    for layer in propagateLayers:
        if layer.log and layer.active:
            layer.writeLog(self)