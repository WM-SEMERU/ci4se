def activate_classification(self, exposure, classification=None):
    if self.layer_mode == layer_mode_continuous:
        selected_unit = self.parent.step_kw_unit.selected_unit()['key']
        target = self.thresholds.get(exposure['key'])
        if target is None:
            self.thresholds[exposure['key']] = {}
        target = self.thresholds.get(exposure['key'])
    else:
        selected_unit = None
        target = self.value_maps.get(exposure['key'])
        if target is None:
            self.value_maps[exposure['key']] = {}
        target = self.value_maps.get(exposure['key'])
    if classification is not None:
        if classification['key'] not in target:
            if self.layer_mode == layer_mode_continuous:
                default_classes = default_classification_thresholds(
                    classification, selected_unit)
                target[classification['key']] = {'classes': default_classes,
                    'active': True}
            else:
                target[classification['key']] = {'classes': {}, 'active': True}
            return
    for classification_key, value in list(target.items()):
        if classification is None:
            value['active'] = False
            continue
        if classification_key == classification['key']:
            value['active'] = True
        else:
            value['active'] = False