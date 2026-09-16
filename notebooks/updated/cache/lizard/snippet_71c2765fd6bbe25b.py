def copy_layer(source, target):
    out_feature = QgsFeature()
    target.startEditing()
    request = QgsFeatureRequest()
    aggregation_layer = False
    if source.keywords.get('layer_purpose') == 'aggregation':
        try:
            use_selected_only = source.use_selected_features_only
        except AttributeError:
            use_selected_only = False
        if use_selected_only and source.selectedFeatureCount() > 0:
            request.setFilterFids(source.selectedFeatureIds())
        aggregation_layer = True
    for i, feature in enumerate(source.getFeatures(request)):
        geom = feature.geometry()
        if aggregation_layer and feature.hasGeometry():
            was_valid, geom = geometry_checker(geom)
            if not geom:
                LOGGER.info(
                    'One geometry in the aggregation layer is still invalid after cleaning.'
                    )
        out_feature.setGeometry(geom)
        out_feature.setAttributes(feature.attributes())
        target.addFeature(out_feature)
    target.commitChanges()