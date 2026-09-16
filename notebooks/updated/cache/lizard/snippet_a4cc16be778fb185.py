def cell_strings(term):
    num_colors = term.number_of_colors
    if num_colors >= 16:
        funcs = term.on_bright_red, term.on_bright_green, term.on_bright_cyan
    elif num_colors >= 8:
        funcs = term.on_red, term.on_green, term.on_blue
    else:
        return term.reverse(' '), term.smacs + term.reverse('a'
            ) + term.rmacs, term.smacs + 'a' + term.rmacs
    return [f(' ') for f in funcs]