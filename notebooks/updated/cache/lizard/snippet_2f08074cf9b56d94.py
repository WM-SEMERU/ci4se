def identify(self, geometry, mapExtent, imageDisplay, tolerance,
    geometryType='esriGeometryPoint', sr=None, layerDefs=None, time=None,
    layerTimeOptions=None, layers='top', returnGeometry=True,
    maxAllowableOffset=None, geometryPrecision=None, dynamicLayers=None,
    returnZ=False, returnM=False, gdbVersion=None):
    params = {'f': 'json', 'geometry': geometry, 'geometryType':
        geometryType, 'tolerance': tolerance, 'mapExtent': mapExtent,
        'imageDisplay': imageDisplay}
    if layerDefs is not None:
        params['layerDefs'] = layerDefs
    if layers is not None:
        params['layers'] = layers
    if sr is not None:
        params['sr'] = sr
    if time is not None:
        params['time'] = time
    if layerTimeOptions is not None:
        params['layerTimeOptions'] = layerTimeOptions
    if maxAllowableOffset is not None:
        params['maxAllowableOffset'] = maxAllowableOffset
    if geometryPrecision is not None:
        params['geometryPrecision'] = geometryPrecision
    if dynamicLayers is not None:
        params['dynamicLayers'] = dynamicLayers
    if gdbVersion is not None:
        params['gdbVersion'] = gdbVersion
    identifyURL = self._url + '/identify'
    return self._get(url=identifyURL, param_dict=params, securityHandler=
        self._securityHandler, proxy_url=self._proxy_url, proxy_port=self.
        _proxy_port)