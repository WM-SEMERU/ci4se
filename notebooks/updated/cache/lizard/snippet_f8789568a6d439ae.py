def _format_number_si(num, n_signif_figures):
    if math.isnan(num) or math.isinf(num):
        return str(num)
    leading, exp = '{:E}'.format(num).split('E')
    leading = round(float(leading), n_signif_figures - 1)
    exp = exp[:1] + exp[2:] if exp[1] == '0' else exp
    formatted = '{}e{}'.format(leading, exp.lstrip('+'))
    return formatted