def _braket_fmt(self, expr_type):
    mapping = {True: {'bra': {True: '\\Bra{{{label}}}^{{({space})}}',
        'subscript': '\\Bra{{{label}}}_{{({space})}}', False:
        '\\Bra{{{label}}}'}, 'ket': {True: '\\Ket{{{label}}}^{{({space})}}',
        'subscript': '\\Ket{{{label}}}_{{({space})}}', False:
        '\\Ket{{{label}}}'}, 'ketbra': {True:
        '\\Ket{{{label_i}}}\\!\\Bra{{{label_j}}}^{{({space})}}',
        'subscript':
        '\\Ket{{{label_i}}}\\!\\Bra{{{label_j}}}_{{({space})}}', False:
        '\\Ket{{{label_i}}}\\!\\Bra{{{label_j}}}'}, 'braket': {True:
        '\\Braket{{{label_i} | {label_j}}}^({space})', 'subscript':
        '\\Braket{{{label_i} | {label_j}}}_({space})', False:
        '\\Braket{{{label_i} | {label_j}}}'}}, False: {'bra': {True:
        '\\left\\langle {label} \\right\\rvert^{{({space})}}', 'subscript':
        '\\left\\langle {label} \\right\\rvert^{{({space})}}', False:
        '\\left\\langle {label} \\right\\rvert'}, 'ket': {True:
        '\\left\\lvert {label} \\right\\rangle^{{({space})}}', 'subscript':
        '\\left\\lvert {label} \\right\\rangle_{{({space})}}', False:
        '\\left\\lvert {label} \\right\\rangle'}, 'ketbra': {True:
        '\\left\\lvert {label_i} \\middle\\rangle\\!\\middle\\langle {label_j} \\right\\rvert^{{({space})}}'
        , 'subscript':
        '\\left\\lvert {label_i} \\middle\\rangle\\!\\middle\\langle {label_j} \\right\\rvert_{{({space})}}'
        , False:
        '\\left\\lvert {label_i} \\middle\\rangle\\!\\middle\\langle {label_j} \\right\\rvert'
        }, 'braket': {True:
        '\\left\\langle {label_i} \\middle\\vert {label_j} \\right\\rangle^{{({space})}}'
        , 'subscript':
        '\\left\\langle {label_i} \\middle\\vert {label_j} \\right\\rangle_{{({space})}}'
        , False:
        '\\left\\langle {label_i} \\middle\\vert {label_j} \\right\\rangle'}}}
    hs_setting = bool(self._settings['show_hs_label'])
    if self._settings['show_hs_label'] == 'subscript':
        hs_setting = 'subscript'
    return mapping[self._settings['tex_use_braket']][expr_type][hs_setting]