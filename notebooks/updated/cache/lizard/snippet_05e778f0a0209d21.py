def quick_layout_settings(self):
    get = CONF.get
    set_ = CONF.set
    section = 'quick_layouts'
    names = get(section, 'names')
    order = get(section, 'order')
    active = get(section, 'active')
    dlg = self.dialog_layout_settings(self, names, order, active)
    if dlg.exec_():
        set_(section, 'names', dlg.names)
        set_(section, 'order', dlg.order)
        set_(section, 'active', dlg.active)
        self.quick_layout_set_menu()