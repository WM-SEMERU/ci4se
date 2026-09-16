def __prepare_args(self, args):
    ret = []
    for a in args:
        if isinstance(a, six.binary_type):
            if self.__size_expr.match(a):
                ret += [a]
            else:
                ret += [b'"' + a + b'"']
            continue
        ret += [bytes(str(a).encode('utf-8'))]
    return ret