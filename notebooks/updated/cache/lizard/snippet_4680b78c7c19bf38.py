def _resolve_parameters(template_dict, parameter_overrides):
    parameter_values = SamBaseProvider._get_parameter_values(template_dict,
        parameter_overrides)
    supported_intrinsics = {action.intrinsic_name: action() for action in
        SamBaseProvider._SUPPORTED_INTRINSICS}
    return IntrinsicsResolver(parameters=parameter_values,
        supported_intrinsics=supported_intrinsics).resolve_parameter_refs(
        template_dict)