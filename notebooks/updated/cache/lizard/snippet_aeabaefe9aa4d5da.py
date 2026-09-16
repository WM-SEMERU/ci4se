def export_coreml(self, filename):
    from turicreate.toolkits import _coreml_utils
    display_name = 'boosted trees classifier'
    short_description = _coreml_utils._mlmodel_short_description(display_name)
    context = {'mode': 'classification', 'model_type': 'boosted_trees',
        'version': _turicreate.__version__, 'class': self.__class__.
        __name__, 'short_description': short_description, 'user_defined': {
        'turicreate_version': _turicreate.__version__}}
    self._export_coreml_impl(filename, context)