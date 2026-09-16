def recipe_status(backend):
    kitchen = DKCloudCommandRunner.which_kitchen_name()
    if kitchen is None:
        raise click.ClickException('You are not in a Kitchen')
    recipe_dir = DKRecipeDisk.find_recipe_root_dir()
    if recipe_dir is None:
        raise click.ClickException('You must be in a Recipe folder')
    recipe_name = DKRecipeDisk.find_recipe_name()
    click.secho(
        "%s - Getting the status of Recipe '%s' in Kitchen '%s'\n\tversus directory '%s'"
         % (get_datetime(), recipe_name, kitchen, recipe_dir), fg='green')
    check_and_print(DKCloudCommandRunner.recipe_status(backend.dki, kitchen,
        recipe_name, recipe_dir))