def invoke(config, name, input):
    myname = name or config.name
    click.echo('Invoking ' + myname)
    output = lambder.invoke_function(myname, input)
    click.echo(output)