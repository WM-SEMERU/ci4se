def get_next_step(self):
    layer_purpose = self.parent.step_kw_purpose.selected_purpose()
    if layer_purpose['key'] != layer_purpose_aggregation['key']:
        subcategory = self.parent.step_kw_subcategory.selected_subcategory()
    else:
        subcategory = {'key': None}
    default_inasafe_fields = get_fields(layer_purpose['key'], subcategory[
        'key'], replace_null=True, in_group=False)
    if default_inasafe_fields:
        return self.parent.step_kw_default_inasafe_fields
    return self.parent.step_kw_source