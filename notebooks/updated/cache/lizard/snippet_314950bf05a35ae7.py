def resolve_resource_refs(self, input_dict, supported_resource_refs):
    if not self.can_handle(input_dict):
        return input_dict
    ref_value = input_dict[self.intrinsic_name]
    logical_id, property = self._parse_resource_reference(ref_value)
    if not logical_id:
        return input_dict
    resolved_value = supported_resource_refs.get(logical_id, property)
    if not resolved_value:
        return input_dict
    return {self.intrinsic_name: resolved_value}