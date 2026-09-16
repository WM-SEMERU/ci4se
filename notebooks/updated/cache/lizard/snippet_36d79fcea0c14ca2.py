def _cloneDefaultedParameter(self, original, default):
    if isinstance(original, ChoiceParameter):
        default = [Option(o.description, o.value, o.value in default) for o in
            original.choices]
    return original.clone(default)