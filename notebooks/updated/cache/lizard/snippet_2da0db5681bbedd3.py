def _add_value_enum(self, var, tag):
    if var['ValueEnum'][0] == 's0':
        numvalues_tag = etree.SubElement(tag, 'NumValues')
        numvalues_tag.text = str(int(var['ValueEnum'][-1][-1]) + 1)
    else:
        valueenum_tag = etree.SubElement(tag, 'ValueEnum')
        valueenum_tag.text = ''
        for value in var['ValueEnum']:
            valueenum_tag.text += value + ' '
        valueenum_tag.text = valueenum_tag.text[:-1]