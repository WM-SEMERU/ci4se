def handle_tags(userdata, macros):
    macro_vars = re.findall('@(.*?)@', userdata)
    for macro_var in macro_vars:
        if macro_var == '!all_macros_export':
            macro_var_export_list = []
            for defined_macro in macros:
                macro_var_export_list.append('export %s="%s"' % (
                    defined_macro, macros[defined_macro]))
            macro_var_exports = '\n'.join(macro_var_export_list)
            userdata = userdata.replace('@%s@' % macro_var, macro_var_exports)
        elif macro_var == '!all_macros_docker':
            macro_var_export_list = []
            for defined_macro in macros:
                macro_var_export_list.append("-e '%s=%s'" % (defined_macro,
                    macros[defined_macro]))
            macro_var_exports = ' '.join(macro_var_export_list)
            userdata = userdata.replace('@%s@' % macro_var, macro_var_exports)
        elif '|' in macro_var:
            macro_var, default_value = macro_var.split('|')
            if macro_var not in macros:
                logging.warning('Using default variable value %s for @%s@ ',
                    default_value, macro_var)
                value = default_value
            else:
                value = macros[macro_var]
            userdata = userdata.replace('@%s|%s@' % (macro_var,
                default_value), value)
        else:
            if macro_var not in macros:
                logging.error('Undefined variable @%s@ in UserData script',
                    macro_var)
                return None
            userdata = userdata.replace('@%s@' % macro_var, macros[macro_var])
    return userdata