def exec_(controller, cmd, *args):
    controller.logger.info('Executing: {0} {1}', cmd, ' '.join(args))
    try:
        subprocess.check_call([cmd] + list(args))
    except (OSError, subprocess.CalledProcessError) as err:
        controller.logger.error('Failed to execute process: {0}', err)