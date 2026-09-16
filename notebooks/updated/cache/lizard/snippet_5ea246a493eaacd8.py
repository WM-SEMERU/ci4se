def _model_for_CLASS(self, name, definition):
    return _ClassModel.from_swagger(self.pclass_for_definition, name,
        definition)