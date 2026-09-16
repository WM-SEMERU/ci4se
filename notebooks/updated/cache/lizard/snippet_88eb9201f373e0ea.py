def make_processor(self, name, mappings, processor_type, **kwargs):
    from .processor import Processor
    if self.processors.get(name):
        raise LookupError('processor has already been created')
    if isinstance(mappings, list):
        mappings = [self.get_rml(item) for item in mappings]
    else:
        mappings = [self.get_rml(mappings)]
    self.processors[name] = Processor[processor_type](mappings, **kwargs)
    self.processors[name].name = name
    return self.processors[name]