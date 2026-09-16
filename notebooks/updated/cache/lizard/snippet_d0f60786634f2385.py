def _error_if_symbol_unused(symbol_word, technical_words_dictionary,
    line_offset, col_offset):
    result = technical_words_dictionary.corrections(symbol_word, distance=5,
        prefix=0)
    if not result.valid:
        return SpellcheckError(symbol_word, line_offset, col_offset, result
            .suggestions, SpellcheckError.TechnicalWord)