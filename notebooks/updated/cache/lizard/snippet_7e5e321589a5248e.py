def fix_config(self, options):
    options = super(Trigger, self).fix_config(options)
    opt = 'condition'
    if opt not in options:
        options[opt] = 'True'
    if opt not in self.help:
        self.help[opt] = (
            "The (optional) condition for teeing off the tokens; uses the 'eval' method, ie the expression must evaluate to a boolean value; storage values placeholders '@{...}' get replaced with their string representations before evaluating the expression (string)."
            )
    return options