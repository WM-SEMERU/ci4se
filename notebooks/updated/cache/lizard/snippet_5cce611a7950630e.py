def option_hook(self, function):
    sig = Signature(function)
    if 'options' not in sig.arguments:
        raise KeyError(
            "option_hook functions must have an argument called 'options', but got {}"
            .format(sig.arguments))
    self.option_hooks.append(function)
    return function