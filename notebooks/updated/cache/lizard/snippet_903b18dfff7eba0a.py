def _formatVals(self, val_list):
    vals = []
    for name, val in val_list:
        if val is not None:
            if isinstance(val, float):
                vals.append('%s.value %f' % (name, val))
            else:
                vals.append('%s.value %s' % (name, val))
        else:
            vals.append('%s.value U' % (name,))
    return '\n'.join(vals)