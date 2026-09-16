def temp(dev, target):
    click.echo('Current target temp: %s' % dev.target_temperature)
    if target:
        click.echo('Setting target temp: %s' % target)
        dev.target_temperature = target