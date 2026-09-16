def print_ast(f):
    for linenum, indent, value in iter_lines(f):
        print('{0}{1}|{2}'.format(str(linenum).rjust(3), ' ' * indent, value))