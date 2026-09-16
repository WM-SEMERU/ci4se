def result_key_for(self, op_name):
    ops = self.resource_data.get('operations', {})
    op = ops.get(op_name, {})
    key = op.get('result_key', None)
    return key