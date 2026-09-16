def on_display_n_changed(self, combo):
    i = combo.get_active_iter()
    if not i:
        return
    model = combo.get_model()
    first_item_path = model.get_path(model.get_iter_first())
    if model.get_path(i) == first_item_path:
        val_int = ALWAYS_ON_PRIMARY
    else:
        val = model.get_value(i, 0)
        val_int = int(val.split()[0])
    self.settings.general.set_int('display-n', val_int)