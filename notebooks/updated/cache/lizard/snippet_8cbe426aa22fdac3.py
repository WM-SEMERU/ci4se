def create(ctx, scenario_name, driver_name):
    args = ctx.obj.get('args')
    subcommand = base._get_subcommand(__name__)
    command_args = {'subcommand': subcommand, 'driver_name': driver_name}
    base.execute_cmdline_scenarios(scenario_name, args, command_args)