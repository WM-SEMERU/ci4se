def reloc_var(var_name, reloc_delta, pointer, var_type):
    template = '{0} {3}{1} = RELOC_VAR(_{1}, {2}, {0});\n'
    return template.format(var_type, var_name, reloc_delta, '*' if pointer else
        '')