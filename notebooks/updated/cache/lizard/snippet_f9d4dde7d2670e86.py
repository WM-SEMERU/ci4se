def resolve_include(self, t):
    s = t[1]
    while not s[0] in '<"':
        try:
            s = self.cpp_namespace[s]
        except KeyError:
            m = function_name.search(s)
            s = self.cpp_namespace[m.group(1)]
            if callable(s):
                args = function_arg_separator.split(m.group(2))
                s = s(*args)
        if not s:
            return None
    return t[0], s[0], s[1:-1]