def NewOutputModule(cls, name, output_mediator):
    output_class = cls.GetOutputClass(name)
    return output_class(output_mediator)