def add_recipe_folder(self, recipe_folder, whitelist=None):
    if whitelist is not None:
        whitelist = set(whitelist)
    if recipe_folder == '':
        recipe_folder = '.'
    for yaml_file in [x for x in os.listdir(recipe_folder) if x.endswith(
        '.yaml')]:
        if whitelist is not None and yaml_file not in whitelist:
            continue
        recipe = RecipeObject.FromFile(os.path.join(recipe_folder,
            yaml_file), self._recipe_actions, self._recipe_resources)
        self._recipes[recipe.name] = recipe
    for ship_file in [x for x in os.listdir(recipe_folder) if x.endswith(
        '.ship')]:
        if whitelist is not None and ship_file not in whitelist:
            continue
        recipe = RecipeObject.FromArchive(os.path.join(recipe_folder,
            ship_file), self._recipe_actions, self._recipe_resources)
        self._recipes[recipe.name] = recipe