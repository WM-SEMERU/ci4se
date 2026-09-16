def process_vm_json(self, json_dict, **kwargs):
    mrf_lines = convert_vm_json_to_mrf(json_dict)
    return self.process_mrf_lines(mrf_lines, **kwargs)