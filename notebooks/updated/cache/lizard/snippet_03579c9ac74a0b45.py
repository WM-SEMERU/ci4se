def recipe_conflicts(backend):
    recipe_dir = DKRecipeDisk.find_recipe_root_dir()
    if recipe_dir is None:
        raise click.ClickException('You must be in a Recipe folder.')
    recipe_name = DKRecipeDisk.find_recipe_name()
    click.secho("%s - Checking for conflicts on Recipe '%s'" % (
        get_datetime(), recipe_name))
    recipe_name = DKRecipeDisk.find_recipe_name()
    check_and_print(DKCloudCommandRunner.get_unresolved_conflicts(
        recipe_name, recipe_dir))