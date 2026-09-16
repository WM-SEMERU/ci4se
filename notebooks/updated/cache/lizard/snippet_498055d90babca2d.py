def on_lstFields_itemSelectionChanged(self):
    self.clear_further_steps()
    field_names = self.selected_fields()
    layer_purpose = self.parent.step_kw_purpose.selected_purpose()
    if not field_names:
        self.parent.pbnNext.setEnabled(False)
        self.lblDescribeField.setText('')
        return
    if not isinstance(field_names, list):
        field_names = [field_names]
    field_descriptions = ''
    feature_count = self.parent.layer.featureCount()
    for field_name in field_names:
        layer_fields = self.parent.layer.fields()
        field_index = layer_fields.indexFromName(field_name)
        if field_index < 0:
            return
        field_type = layer_fields.field(field_name).typeName()
        field_index = layer_fields.indexFromName(field_name)
        unique_values = self.parent.layer.uniqueValues(field_index)
        unique_values_str = [(i is not None and str(i) or 'NULL') for i in
            list(unique_values)[0:48]]
        unique_values_str = ', '.join(unique_values_str)
        field_descriptions += tr('<b>Field name</b>: {field_name}').format(
            field_name=field_name)
        field_descriptions += tr('<br><b>Field type</b>: {field_type}').format(
            field_type=field_type)
        if feature_count != -1 and layer_purpose == layer_purpose_aggregation:
            if len(unique_values) == feature_count:
                unique = tr('Yes')
            else:
                unique = tr('No')
            field_descriptions += tr(
                '<br><b>Unique</b>: {unique} ({unique_values_count} unique values from {feature_count} features)'
                .format(unique=unique, unique_values_count=len(
                unique_values), feature_count=feature_count))
        field_descriptions += tr(
            '<br><b>Unique values</b>: {unique_values_str}<br><br>').format(
            unique_values_str=unique_values_str)
    self.lblDescribeField.setText(field_descriptions)
    self.parent.pbnNext.setEnabled(True)