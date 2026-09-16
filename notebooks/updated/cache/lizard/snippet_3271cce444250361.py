def set_default_config(*, style=_UNSET_SENTINEL, max_seq_len=
    _UNSET_SENTINEL, width=_UNSET_SENTINEL, ribbon_width=_UNSET_SENTINEL,
    depth=_UNSET_SENTINEL, sort_dict_keys=_UNSET_SENTINEL):
    global _default_config
    if style is not _UNSET_SENTINEL:
        set_default_style(style)
    new_defaults = {**_default_config}
    if max_seq_len is not _UNSET_SENTINEL:
        new_defaults['max_seq_len'] = max_seq_len
    if width is not _UNSET_SENTINEL:
        new_defaults['width'] = width
    if ribbon_width is not _UNSET_SENTINEL:
        new_defaults['ribbon_width'] = ribbon_width
    if depth is not _UNSET_SENTINEL:
        new_defaults['depth'] = depth
    if sort_dict_keys is not _UNSET_SENTINEL:
        new_defaults['sort_dict_keys'] = sort_dict_keys
    _default_config = new_defaults
    return new_defaults