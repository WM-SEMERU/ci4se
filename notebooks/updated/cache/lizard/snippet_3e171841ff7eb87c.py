def compile(self, source_code, post_treatment=''.join):
    structure = self._structure(source_code)
    values = self._struct_to_values(structure, source_code)
    obj_code = langspec.translated(structure, values, self.target_lang_spec)
    return obj_code if post_treatment is None else post_treatment(obj_code)