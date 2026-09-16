def get_next_step(self):
    subcategory = self.parent.step_kw_subcategory.selected_subcategory()
    is_raster = is_raster_layer(self.parent.layer)
    has_classifications = get_classifications(subcategory['key'])
    if not is_raster:
        return self.parent.step_kw_field
    elif has_classifications:
        return self.parent.step_kw_multi_classifications
    return self.parent.step_kw_source