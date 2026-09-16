def GetOutputClasses(cls):
    for _, output_class in iter(cls._output_classes.items()):
        yield output_class.NAME, output_class