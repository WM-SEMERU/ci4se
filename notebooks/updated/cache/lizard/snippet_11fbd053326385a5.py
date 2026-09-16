def setup(self):
    for language in self.languages:
        self.index_name = self._index_name_for_language(language)
        try:
            self.existing_mapping[language] = self.conn.indices.get_mapping(
                index=self.index_name)
        except NotFoundError:
            pass
        except Exception:
            if not self.silently_fail:
                raise
        unified_index = haystack.connections[self.connection_alias
            ].get_unified_index()
        self.content_field_name, field_mapping = self.build_schema(
            unified_index.all_searchfields(), language)
        current_mapping = {'modelresult': {'properties': field_mapping,
            '_boost': {'name': 'boost', 'null_value': 1.0}}}
        if current_mapping != self.existing_mapping[language]:
            try:
                self.conn.indices.create(index=self.index_name, body=self.
                    DEFAULT_SETTINGS, ignore=400)
                self.conn.indices.put_mapping(index=self.index_name,
                    doc_type='modelresult', body=current_mapping)
                self.existing_mapping[language] = current_mapping
            except Exception:
                if not self.silently_fail:
                    raise
    self.setup_complete = True