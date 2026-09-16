def create_profile_layer(profiling):
    fields = [create_field_from_definition(profiling_function_field),
        create_field_from_definition(profiling_time_field)]
    if setting(key='memory_profile', expected_type=bool):
        fields.append(create_field_from_definition(profiling_memory_field))
    tabular = create_memory_layer('profiling', QgsWkbTypes.NullGeometry,
        fields=fields)
    tabular.keywords['layer_purpose'] = layer_purpose_profiling['key']
    tabular.keywords['title'] = layer_purpose_profiling['name']
    if qgis_version() >= 21800:
        tabular.setName(tabular.keywords['title'])
    else:
        tabular.setLayerName(tabular.keywords['title'])
    tabular.keywords['inasafe_fields'] = {profiling_function_field['key']:
        profiling_function_field['field_name'], profiling_time_field['key']:
        profiling_time_field['field_name']}
    if setting(key='memory_profile', expected_type=bool):
        tabular.keywords['inasafe_fields'][profiling_memory_field['key']
            ] = profiling_memory_field['field_name']
    tabular.keywords[inasafe_keyword_version_key] = inasafe_keyword_version
    table = profiling.to_text().splitlines()[3:]
    tabular.startEditing()
    for line in table:
        feature = QgsFeature()
        items = line.split(', ')
        time = items[1].replace('-', '')
        if setting(key='memory_profile', expected_type=bool):
            memory = items[2].replace('-', '')
            feature.setAttributes([items[0], time, memory])
        else:
            feature.setAttributes([items[0], time])
        tabular.addFeature(feature)
    tabular.commitChanges()
    return tabular