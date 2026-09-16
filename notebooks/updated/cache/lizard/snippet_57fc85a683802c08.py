def _set_combobox(self, attrname, vals, default=0):
    combobox = getattr(self.w, attrname)
    for val in vals:
        combobox.append_text(val)
    if default > len(vals):
        default = 0
    val = vals[default]
    combobox.show_text(val)
    return val