def actors(context):
    fritz = context.obj
    fritz.login()
    for actor in fritz.get_actors():
        click.echo('{} ({} {}; AIN {} )'.format(actor.name, actor.
            manufacturer, actor.productname, actor.actor_id))
        if actor.has_temperature:
            click.echo('Temp: act {} target {}; battery (low): {}'.format(
                actor.temperature, actor.target_temperature, actor.battery_low)
                )
            click.echo('Temp (via get): act {} target {}'.format(actor.
                get_temperature(), actor.get_target_temperature()))