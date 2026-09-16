def _format_number(num, n_signif_figures, max_width):
    if max_width < 6:
        raise NotImplementedError(
            'Guaranteed formatting in fewer than 6 characters not supported.')
    if math.isnan(num) or math.isinf(num):
        return str(num)
    n_digits = lambda num: math.floor(math.log10(abs(num) + 0.5)) + 1
    if abs(num) > 10 ** -n_signif_figures and n_digits(num
        ) <= max_width - n_signif_figures:
        return str(round(num, n_signif_figures))[:max_width].rstrip('.')
    elif _number_width(num) <= max_width:
        if n_digits(num) >= n_signif_figures:
            return str(int(round(num)))
        else:
            return str(num)
    else:
        return _format_number_si(num, n_signif_figures)