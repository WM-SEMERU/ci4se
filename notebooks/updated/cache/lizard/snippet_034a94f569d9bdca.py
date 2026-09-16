def parse(code, module_name='', path=None, apply_transforms=True):
    code = textwrap.dedent(code)
    builder = AstroidBuilder(manager=MANAGER, apply_transforms=apply_transforms
        )
    return builder.string_build(code, modname=module_name, path=path)