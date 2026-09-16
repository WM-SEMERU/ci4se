def _expand_api(self, api, receiver, args, pseudo_type, equivalent):
    if callable(api):
        if receiver:
            return api(receiver, *(args + [pseudo_type]))
        else:
            return api(*(args + [pseudo_type]))
    elif isinstance(api, str):
        if '(' in api:
            call_api, arg_code = api[:-1].split('(')
            new_args = [self._parse_part(a.strip(), receiver, args,
                equivalent) for a in arg_code.split(',')]
        else:
            call_api, arg_code = api, ''
            new_args = args
        if '#' in call_api:
            a, b = call_api.split('#')
            method_receiver = self._parse_part(a, receiver, args, equivalent
                ) if a else receiver
            return method_call(method_receiver, b, new_args, pseudo_type=
                pseudo_type)
        elif '.' in call_api:
            a, b = call_api.split('.')
            static_receiver = self._parse_part(a, receiver, args, equivalent
                ) if a else receiver
            if b[-1] != '!':
                return Node('static_call', receiver=static_receiver,
                    message=b, args=new_args, pseudo_type=pseudo_type)
            else:
                return Node('attr', object=static_receiver, attr=b[:-1],
                    pseudo_type=pseudo_type)
        elif receiver:
            return call(call_api, [receiver] + new_args, pseudo_type=
                pseudo_type)
        else:
            return call(call_api, new_args, pseudo_type=pseudo_type)
    else:
        raise PseudoDSLError('%s not supported by api dsl' % str(api))