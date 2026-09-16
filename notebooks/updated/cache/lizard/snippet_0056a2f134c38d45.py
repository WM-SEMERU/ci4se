def format_stack_frame_json(self):
    stack_frame_json = {}
    stack_frame_json['function_name'] = get_truncatable_str(self.func_name)
    stack_frame_json['original_function_name'] = get_truncatable_str(self.
        original_func_name)
    stack_frame_json['file_name'] = get_truncatable_str(self.file_name)
    stack_frame_json['line_number'] = self.line_num
    stack_frame_json['column_number'] = self.col_num
    stack_frame_json['load_module'] = {'module': get_truncatable_str(self.
        load_module), 'build_id': get_truncatable_str(self.build_id)}
    stack_frame_json['source_version'] = get_truncatable_str(self.
        source_version)
    return stack_frame_json