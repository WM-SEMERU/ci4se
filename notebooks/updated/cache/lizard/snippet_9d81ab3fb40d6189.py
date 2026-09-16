def default_unit_label(axis, unit):
    if not axis.isDefault_label:
        return
    label = axis.set_label_text(unit.to_string('latex_inline_dimensional'))
    axis.isDefault_label = True
    return label.get_text()