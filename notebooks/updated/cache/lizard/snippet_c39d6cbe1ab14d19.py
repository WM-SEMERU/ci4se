def set_widgets(self):
    self.clear_further_steps()
    purpose = self.parent.step_kw_purpose.selected_purpose()
    subcategory = self.parent.step_kw_subcategory.selected_subcategory()
    self.lblSelectUnit.setText(unit_question % (subcategory['name'],
        purpose['name']))
    self.lblDescribeUnit.setText('')
    self.lstUnits.clear()
    subcat = self.parent.step_kw_subcategory.selected_subcategory()['key']
    if purpose == layer_purpose_hazard:
        units_for_layer = hazard_units(subcat)
    else:
        units_for_layer = exposure_units(subcat)
    for unit_for_layer in units_for_layer:
        item = QListWidgetItem(unit_for_layer['name'], self.lstUnits)
        item.setData(QtCore.Qt.UserRole, unit_for_layer['key'])
        self.lstUnits.addItem(item)
    if self.parent.step_kw_purpose.selected_purpose() == layer_purpose_hazard:
        key = continuous_hazard_unit['key']
    else:
        key = exposure_unit['key']
    unit_id = self.parent.get_existing_keyword(key)
    if unit_id:
        units = []
        for index in range(self.lstUnits.count()):
            item = self.lstUnits.item(index)
            units.append(item.data(QtCore.Qt.UserRole))
        if unit_id in units:
            self.lstUnits.setCurrentRow(units.index(unit_id))
    self.auto_select_one_item(self.lstUnits)