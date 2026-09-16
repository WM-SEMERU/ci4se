def cli(ctx, board, fpga, pack, type, size, project_dir, verbose,
    verbose_yosys, verbose_arachne):
    exit_code = SCons(project_dir).time({'board': board, 'fpga': fpga,
        'size': size, 'type': type, 'pack': pack, 'verbose': {'all':
        verbose, 'yosys': verbose_yosys, 'arachne': verbose_arachne}})
    ctx.exit(exit_code)