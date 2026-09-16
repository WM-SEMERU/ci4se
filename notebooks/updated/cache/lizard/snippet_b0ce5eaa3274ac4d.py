def transform(input_fragment, parameter_values, managed_policy_loader):
    sam_parser = Parser()
    translator = Translator(managed_policy_loader.load(), sam_parser)
    return translator.translate(input_fragment, parameter_values=
        parameter_values)