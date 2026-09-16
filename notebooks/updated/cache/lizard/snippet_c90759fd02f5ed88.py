def get_outputs(self, merge_multi_context=True, begin=0, end=None):
    if end is None:
        end = self.num_outputs
    outputs = [[exec_.outputs[i] for exec_ in self.execs] for i in range(
        begin, end)]
    if merge_multi_context:
        outputs = _merge_multi_context(outputs, self.output_layouts)
    return outputs