def main():
    conf = init_and_get_conf()
    logger = make_logger(__name__)
    logger.info('YaBT version {}', __version__)
    handlers = {'build': YabtCommand(func=cmd_build, requires_project=True),
        'dot': YabtCommand(func=cmd_dot, requires_project=True), 'test':
        YabtCommand(func=cmd_test, requires_project=True), 'tree':
        YabtCommand(func=cmd_tree, requires_project=True), 'version':
        YabtCommand(func=cmd_version, requires_project=False),
        'list-builders': YabtCommand(func=cmd_list, requires_project=False)}
    command = handlers[conf.cmd]
    if command.requires_project and not conf.in_yabt_project():
        fatal('Not a YABT project (or any of the parent directories): {}',
            BUILD_PROJ_FILE)
    try:
        command.func(conf)
    except Exception as ex:
        fatal('{}', ex)