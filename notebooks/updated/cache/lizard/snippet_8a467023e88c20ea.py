def from_bytes_list(cls, function_descriptor_list):
    assert isinstance(function_descriptor_list, list)
    if len(function_descriptor_list) == 0:
        return FunctionDescriptor.for_driver_task()
    elif len(function_descriptor_list) == 3 or len(function_descriptor_list
        ) == 4:
        module_name = ensure_str(function_descriptor_list[0])
        class_name = ensure_str(function_descriptor_list[1])
        function_name = ensure_str(function_descriptor_list[2])
        if len(function_descriptor_list) == 4:
            return cls(module_name, function_name, class_name,
                function_descriptor_list[3])
        else:
            return cls(module_name, function_name, class_name)
    else:
        raise Exception('Invalid input for FunctionDescriptor.from_bytes_list')