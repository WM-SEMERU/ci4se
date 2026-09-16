def build_model_name(cls, name='modelName', output_name='output'):
    obj = cls(name)
    obj.exporter = 'generate_model_name'
    obj.output_name = output_name
    return obj