def return_handler(self, call_node, function_nodes,
    saved_function_call_index, first_node):
    if any(isinstance(node, YieldNode) for node in function_nodes):
        rhs_prefix = 'yld_'
    elif any(isinstance(node, ConnectToExitNode) for node in function_nodes):
        rhs_prefix = 'ret_'
    else:
        return
    LHS = CALL_IDENTIFIER + 'call_' + str(saved_function_call_index)
    RHS = rhs_prefix + get_call_names_as_string(call_node.func)
    return_node = RestoreNode(LHS + ' = ' + RHS, LHS, [RHS], line_number=
        call_node.lineno, path=self.filenames[-1])
    return_node.first_node = first_node
    self.nodes[-1].connect(return_node)
    self.nodes.append(return_node)