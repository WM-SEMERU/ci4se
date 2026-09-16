def endswith(self, pat):
    check_type(pat, str)
    return _series_bool_result(self, weld_str_endswith, pat=pat)