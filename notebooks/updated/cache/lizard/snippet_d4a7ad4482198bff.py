def _speak_as_spell_out_inherit(self, element):
    self._reverse_speak_as(element, 'spell-out')
    self._isolate_text_node(element)
    self._visit(element, self._speak_as_spell_out)