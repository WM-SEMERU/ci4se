def _get_arg_info(self):
    ret_dict = {'args': [], 'line': 'Unknown', 'file': 'Unknown',
        'arg_names': []}
    arg_vals = self.arg_vals
    c = self.call
    ret_dict.update(c.info)
    if len(arg_vals) > 0:
        args = []
        if len(ret_dict['arg_names']) > 0:
            for i, arg_name in enumerate(ret_dict['arg_names']):
                args.append({'name': arg_name, 'val': arg_vals[i]})
        else:
            for i, arg_val in enumerate(arg_vals):
                args.append({'name': 'Unknown {}'.format(i), 'val': arg_val})
        ret_dict['args'] = args
    return ret_dict