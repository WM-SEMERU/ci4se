def subcategories_for_layer(self):
    purpose = self.parent.step_kw_purpose.selected_purpose()
    layer_geometry_key = self.parent.get_layer_geometry_key()
    if purpose == layer_purpose_hazard:
        return hazards_for_layer(layer_geometry_key)
    elif purpose == layer_purpose_exposure:
        return exposures_for_layer(layer_geometry_key)