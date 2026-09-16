def parse_config(self, config):
    self.remove_xml_tags = config.get('gtk_doc_remove_xml')
    self.escape_html = config.get('gtk_doc_escape_html')
    self.gdbus_codegen_sources = config.get_paths('gdbus_codegen_sources')