def translate(self, instruction):
    try:
        trans_instrs = self._translate(instruction)
    except Exception:
        self._log_translation_exception(instruction)
        raise TranslationError('Unknown error')
    return trans_instrs