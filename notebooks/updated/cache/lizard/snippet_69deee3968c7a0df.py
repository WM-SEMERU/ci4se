def callback_checkbox(attr, old, new):
    import numpy
    for i in range(len(lines)):
        lines[i].visible = i in param_checkbox.active
        scats[i].visible = i in param_checkbox.active
    return None