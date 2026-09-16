def get_scalar_mirrored_target_option(self, option_name, target):
    mirrored_option_declaration = self._mirrored_option_declarations[
        option_name]
    return mirrored_option_declaration.get_mirrored_scalar_option_value(target)