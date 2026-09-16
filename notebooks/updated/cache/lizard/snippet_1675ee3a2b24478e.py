def set_widgets(self):
    self.clear_further_steps()
    purpose = self.parent.step_kw_purpose.selected_purpose()
    subcategory = self.parent.step_kw_subcategory.selected_subcategory()
    layer_mode_question = layer_mode_raster_question if is_raster_layer(self
        .parent.layer) else layer_mode_vector_question
    self.lblDescribeLayerMode.setText('')
    self.lstLayerModes.clear()
    layer_modes = get_layer_modes(subcategory['key'])
    if is_raster_layer(self.parent.layer):
        layer_mode_question = layer_mode_raster_question
    elif len(layer_modes) == 2:
        layer_mode_question = layer_mode_vector_question
    elif len(layer_modes) == 1:
        if layer_modes[0]['key'] == 'classified':
            layer_mode_question = layer_mode_vector_classified_confirm
        elif layer_modes[0]['key'] == 'continuous':
            layer_mode_question = layer_mode_vector_continuous_confirm
        else:
            layer_mode_question = layer_mode_vector_question
    self.lblSelectLayerMode.setText(layer_mode_question % (subcategory[
        'name'], purpose['name']))
    for layer_mode in layer_modes:
        item = QListWidgetItem(layer_mode['name'], self.lstLayerModes)
        item.setData(QtCore.Qt.UserRole, layer_mode['key'])
        self.lstLayerModes.addItem(item)
    layer_mode_keys = [m['key'] for m in layer_modes]
    layer_mode_keyword = self.parent.get_existing_keyword('layer_mode')
    if layer_mode_keyword in layer_mode_keys:
        index = layer_mode_keys.index(layer_mode_keyword)
    elif layer_mode_continuous['key'] in layer_mode_keys:
        index = layer_mode_keys.index(layer_mode_continuous['key'])
    else:
        index = -1
    self.lstLayerModes.setCurrentRow(index)
    self.auto_select_one_item(self.lstLayerModes)