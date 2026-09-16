def to_latex(self):
    latex = '[{} '
    for attribute, value in self:
        if attribute in ['speaker_model', 'is_in_commonground']:
            continue
        value_l = value.to_latex()
        if value_l == '':
            continue
        latex += '{attribute:<15} &  {value:<20} \\\\ \n'.format(attribute=
            attribute, value=value_l)
    latex += ']\n'
    return latex