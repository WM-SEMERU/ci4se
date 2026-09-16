def fetchallarrow(self, strings_as_dictionary=False, adaptive_integers=False):
    self._assert_valid_result_set()
    if _has_arrow_support():
        from turbodbc_arrow_support import make_arrow_result_set
        return make_arrow_result_set(self.impl.get_result_set(),
            strings_as_dictionary, adaptive_integers).fetch_all()
    else:
        raise Error(_NO_ARROW_SUPPORT_MSG)