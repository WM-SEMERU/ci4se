def create_local_scope_from_def_args(self, call_args, def_args, line_number,
    saved_function_call_index):
    for i in range(len(call_args)):
        def_arg_local_name = def_args[i]
        def_arg_temp_name = 'temp_' + str(saved_function_call_index
            ) + '_' + def_args[i]
        local_scope_node = RestoreNode(def_arg_local_name + ' = ' +
            def_arg_temp_name, def_arg_local_name, [def_arg_temp_name],
            line_number=line_number, path=self.filenames[-1])
        self.nodes[-1].connect(local_scope_node)
        self.nodes.append(local_scope_node)