def inasafe_fields_for_the_layer(self):
    if self.parent.get_layer_geometry_key() == layer_geometry_raster['key']:
        return []
    layer_purpose_key = self.parent.step_kw_purpose.selected_purpose()['key']
    if layer_purpose_key != layer_purpose_aggregation['key']:
        subcategory_key = self.parent.step_kw_subcategory.selected_subcategory(
            )['key']
    else:
        subcategory_key = None
    inasafe_fields = get_fields(layer_purpose_key, subcategory_key,
        replace_null=False, in_group=False)
    try:
        inasafe_fields.remove(get_compulsory_fields(layer_purpose_key,
            subcategory_key))
    except ValueError:
        pass
    return inasafe_fields