def steps_for_spec(builder, spec, processed_modules=None):
    if processed_modules is None:
        processed_modules = set()
    steps = []
    for module in spec.get('depends_on', []):
        if module not in processed_modules:
            processed_modules.add(module)
            steps.extend(steps_for_spec(builder, module.fbcode_builder_spec
                (builder), processed_modules))
    steps.extend(spec.get('steps', []))
    return steps