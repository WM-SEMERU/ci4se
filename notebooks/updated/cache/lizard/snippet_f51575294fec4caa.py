def save_local_scope(self, line_number, saved_function_call_index):
    saved_variables = list()
    saved_variables_so_far = set()
    first_node = None
    for assignment in [node for node in self.nodes if type(node) ==
        AssignmentNode or type(node) == AssignmentCallNode or type(Node) ==
        BBorBInode]:
        if assignment.left_hand_side in saved_variables_so_far:
            continue
        saved_variables_so_far.add(assignment.left_hand_side)
        save_name = 'save_{}_{}'.format(saved_function_call_index,
            assignment.left_hand_side)
        previous_node = self.nodes[-1]
        saved_scope_node = RestoreNode(save_name + ' = ' + assignment.
            left_hand_side, save_name, [assignment.left_hand_side],
            line_number=line_number, path=self.filenames[-1])
        if not first_node:
            first_node = saved_scope_node
        self.nodes.append(saved_scope_node)
        saved_variables.append(SavedVariable(LHS=save_name, RHS=assignment.
            left_hand_side))
        self.connect_if_allowed(previous_node, saved_scope_node)
    return saved_variables, first_node