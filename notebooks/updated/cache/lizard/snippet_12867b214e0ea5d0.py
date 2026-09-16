def compute_memory_contents_under_schedule(self, schedule):
    out_degree = self._compute_initial_out_degree()
    curr_memory_contents = set()
    memory_contents_for_each_operation = []
    for operation_id in schedule:
        operation_name = self._operations[operation_id].name
        for output_name in self.get_operation_output_names(operation_name):
            curr_memory_contents.add(output_name)
        memory_contents_for_each_operation.append(frozenset(
            curr_memory_contents))
        for output_name in self.get_operation_output_names(operation_name):
            if out_degree[output_name] == 0:
                curr_memory_contents.remove(output_name)
        for input_name in self.get_operation_input_names(operation_name):
            out_degree[input_name] -= 1
            if out_degree[input_name] == 0:
                curr_memory_contents.remove(input_name)
    return memory_contents_for_each_operation