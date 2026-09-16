def get_new_selection_attr_state(self, selection, attr_key):
    cell_attributes = self.grid.code_array.cell_attributes
    attr_values = self.attr_toggle_values[attr_key]
    attr_map = dict(zip(attr_values, attr_values[1:] + attr_values[:1]))
    selection_attrs = (attr for attr in cell_attributes if attr[0] == selection
        )
    attrs = {}
    for selection_attr in selection_attrs:
        attrs.update(selection_attr[2])
    if attr_key in attrs:
        return attr_map[attrs[attr_key]]
    else:
        return self.attr_toggle_values[attr_key][1]