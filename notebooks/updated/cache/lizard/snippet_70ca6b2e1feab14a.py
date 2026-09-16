def get_caller_text(frame):

    def find_match_node(node):
        """Find a candidate ast node"""
        match_node = None
        for chd in ast.iter_child_nodes(node):
            if getattr(chd, 'lineno', 0) > frame.f_back.f_lineno:
                break
            match_node = node if isinstance(chd, ast.Name) and isinstance(node,
                ast.Call) else match_node
            match_node = find_match_node(chd) or match_node
        return match_node
    lines, _ = inspect.findsource(frame.f_back.f_code)
    match_node = find_match_node(ast.parse(''.join(lines)))
    return unparse(match_node).strip().replace(', ', ','
        ) if match_node is not None else None