def register_array_types_from_sources(self, source_files):
    for fname in source_files:
        if is_vhdl(fname):
            self._register_array_types(self.extract_objects(fname))