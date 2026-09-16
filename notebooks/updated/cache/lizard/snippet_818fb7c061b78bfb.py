def nvrtcCreateProgram(self, src, name, headers, include_names):
    res = c_void_p()
    headers_array = (c_char_p * len(headers))()
    headers_array[:] = encode_str_list(headers)
    include_names_array = (c_char_p * len(include_names))()
    include_names_array[:] = encode_str_list(include_names)
    code = self._lib.nvrtcCreateProgram(byref(res), c_char_p(encode_str(src
        )), c_char_p(encode_str(name)), len(headers), headers_array,
        include_names_array)
    self._throw_on_error(code)
    return res