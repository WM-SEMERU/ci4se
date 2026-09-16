def add_helpingmaterials(config, helping_materials_file, helping_type):
    res = _add_helpingmaterials(config, helping_materials_file, helping_type)
    click.echo(res)