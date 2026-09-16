def replace_obfuscatables(module, tokens, obfunc, replace, name_generator,
    table=None):
    skip_line = False
    skip_next = False
    right_of_equal = False
    inside_parens = 0
    inside_function = False
    indent = 0
    function_indent = 0
    replacement = next(name_generator)
    for index, tok in enumerate(tokens):
        token_type = tok[0]
        token_string = tok[1]
        if token_type == tokenize.NEWLINE:
            skip_line = False
            right_of_equal = False
            inside_parens = 0
        elif token_type == tokenize.INDENT:
            indent += 1
        elif token_type == tokenize.DEDENT:
            indent -= 1
            if inside_function and function_indent == indent:
                function_indent = 0
                inside_function = False
        if token_string == 'def':
            function_indent = indent
            function_name = tokens[index + 1][1]
            inside_function = function_name
        result = obfunc(tokens, index, replace, replacement, right_of_equal,
            inside_parens, inside_function)
        if result:
            if skip_next:
                skip_next = False
            elif skip_line:
                pass
            elif result == '__skipline__':
                skip_line = True
            elif result == '__skipnext__':
                skip_next = True
            elif result == '__open_paren__':
                right_of_equal = False
                inside_parens += 1
            elif result == '__close_paren__':
                inside_parens -= 1
            elif result == '__comma__':
                right_of_equal = False
            elif result == '__right_of_equal__':
                if not inside_parens:
                    right_of_equal = True
            elif table:
                combined_name = '%s.%s' % (module, token_string)
                try:
                    tokens[index][1] = table[0][combined_name]
                except KeyError:
                    table[0].update({combined_name: result})
                    tokens[index][1] = result
            else:
                tokens[index][1] = result