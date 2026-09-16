def _check_current_value(gnome_kwargs, value):
    current_value = __salt__['gnome.get'](**gnome_kwargs)
    return six.text_type(current_value) == six.text_type(value)