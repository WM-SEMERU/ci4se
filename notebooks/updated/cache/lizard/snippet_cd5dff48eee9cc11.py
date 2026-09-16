def pretty_print_graphql(query, use_four_spaces=True):
    output = visit(parse(query), CustomPrintingVisitor())
    if use_four_spaces:
        return fix_indentation_depth(output)
    return output