def add(self, *args):
    if len(args) > 2:
        name, template = args[:2]
        args = args[2:]
    else:
        name = None
        template = args[0]
        args = args[1:]
    if isinstance(template, tuple):
        template, type_converters = template
        template = Template(template, **type_converters)
    elif not isinstance(template, Template):
        template = Template(template)
    if name:
        self._templates[name] = template
    super(PathRouter, self).add(template, *args)