def _clear(self):
    self._current_output = U_EMPTY_STRING
    self._accrued_input = U_EMPTY_STRING
    self._accrued_input_without_formatting = U_EMPTY_STRING
    self._formatting_template = U_EMPTY_STRING
    self._last_match_position = 0
    self._current_formatting_pattern = U_EMPTY_STRING
    self._prefix_before_national_number = U_EMPTY_STRING
    self._should_add_space_after_national_prefix = False
    self._extracted_national_prefix = U_EMPTY_STRING
    self._national_number = U_EMPTY_STRING
    self._able_to_format = True
    self._input_has_formatting = False
    self._position_to_remember = 0
    self._original_position = 0
    self._is_complete_number = False
    self._is_expecting_country_calling_code = False
    self._possible_formats = []