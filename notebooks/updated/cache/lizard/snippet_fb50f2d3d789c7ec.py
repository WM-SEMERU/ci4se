def tokenize_ofp_instruction_arg(arg):
    arg_re = re.compile('[^,()]*')
    try:
        rest = arg
        result = []
        while len(rest):
            m = arg_re.match(rest)
            if m.end(0) == len(rest):
                result.append(rest)
                return result
            if rest[m.end(0)] == '(':
                this_block, rest = _tokenize_paren_block(rest, m.end(0) + 1)
                result.append(this_block)
            elif rest[m.end(0)] == ',':
                result.append(m.group(0))
                rest = rest[m.end(0):]
            else:
                raise Exception
            if len(rest):
                assert rest[0] == ','
                rest = rest[1:]
        return result
    except Exception:
        raise ryu.exception.OFPInvalidActionString(action_str=arg)