def get_next_step(self):
    if self.selected_purpose() == layer_purpose_aggregation:
        new_step = self.parent.step_kw_field
    else:
        new_step = self.parent.step_kw_subcategory
    return new_step