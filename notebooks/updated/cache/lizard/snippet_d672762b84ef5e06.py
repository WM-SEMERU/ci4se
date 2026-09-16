def load_parameter_definitions(self, sheet_name: str=None):
    definitions = self.excel_handler.load_definitions(sheet_name, filename=
        self.filename)
    self.definition_version = self.excel_handler.version
    return definitions