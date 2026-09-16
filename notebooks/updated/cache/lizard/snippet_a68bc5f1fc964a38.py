def value_from_field_name(field_name, analysis_layer):
    field_index = analysis_layer.fields().lookupField(field_name)
    if field_index < 0:
        return None
    else:
        feat = QgsFeature()
        analysis_layer.getFeatures().nextFeature(feat)
        return feat[field_index]