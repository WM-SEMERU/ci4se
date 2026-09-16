def visualize(ctx, meta_model_file, model_file, ignore_case, output_format):
    debug = ctx.obj['debug']
    meta_model, model = check_model(meta_model_file, model_file, debug,
        ignore_case)
    if output_format == 'plantuml':
        pu_file = '{}.pu'.format(meta_model_file)
        click.echo("Generating '{}' file for meta-model.".format(pu_file))
        click.echo("To convert to png run 'plantuml {}'".format(pu_file))
        click.echo("To convert to svg run 'plantuml -tsvg {}'".format(pu_file))
        metamodel_export(meta_model, pu_file, PlantUmlRenderer())
    else:
        dot_file = '{}.dot'.format(meta_model_file)
        click.echo("Generating '{}' file for meta-model.".format(dot_file))
        click.echo("To convert to png run 'dot -Tpng -O {}'".format(dot_file))
        metamodel_export(meta_model, dot_file)
    if model_file:
        if output_format == 'plantuml':
            raise Exception('plantuml is not supported for model files, yet.')
        dot_file = '{}.dot'.format(model_file)
        click.echo("Generating '{}' file for model.".format(model_file))
        click.echo("To convert to png run 'dot -Tpng -O {}'".format(model_file)
            )
        model_export(model, dot_file)