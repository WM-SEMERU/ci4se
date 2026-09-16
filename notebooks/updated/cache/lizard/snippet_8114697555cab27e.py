def has_requisite_content_models(self):
    for cmodel in getattr(self, 'CONTENT_MODELS', ()):
        if not self.has_model(cmodel):
            return False
    return True