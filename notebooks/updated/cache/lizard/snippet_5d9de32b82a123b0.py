def _speak_as_literal_punctuation(self, element):
    self._speak_as(element, self._get_regular_expression_of_symbols(),
        'literal-punctuation', self._operation_speak_as_literal_punctuation)