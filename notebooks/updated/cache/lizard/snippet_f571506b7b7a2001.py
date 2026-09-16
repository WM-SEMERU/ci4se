def console(gandi, resource):
    gandi.echo(
        "/!\\ Please be aware that if you didn't provide a password during creation, console service will be unavailable."
        )
    gandi.echo('/!\\ You can use "gandi vm update" command to set a password.')
    gandi.echo('/!\\ Use ~. ssh escape key to exit.')
    gandi.iaas.console(resource)