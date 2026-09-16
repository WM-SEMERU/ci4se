def run(self):
    self._prepare()
    for recipe in self._recipes:
        run_recipe = True
        if not self.arguments.yes:
            run_recipe = pypro.console.ask_bool('Run %s.%s' % (recipe.
                module, recipe.name), 'yes')
        if run_recipe:
            recipe.run(self, self.arguments)
    if self.arguments.verbose:
        pypro.console.out(
            'Thanks for using pypro. Support this project at https://github.com/avladev/pypro'
            )