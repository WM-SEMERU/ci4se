def run_command(local_root, command, env_var=True, pipeto=None, retry=0,
    environ=None):
    log = logging.getLogger(__name__)
    env = os.environ.copy()
    if environ:
        env.update(environ)
    if env_var and not IS_WINDOWS:
        env['GIT_DIR'] = os.path.join(local_root, '.git')
    else:
        env.pop('GIT_DIR', None)
    with open(os.devnull) as null:
        main = Popen(command, cwd=local_root, env=env, stdout=PIPE, stderr=
            PIPE if pipeto else STDOUT, stdin=null)
        if pipeto:
            pipeto(main.stdout)
            main_output = main.communicate()[1].decode('utf-8')
        else:
            main_output = main.communicate()[0].decode('utf-8')
    log.debug(json.dumps(dict(cwd=local_root, command=command, code=main.
        poll(), output=main_output)))
    if main.poll() != 0:
        if retry < 1:
            raise CalledProcessError(main.poll(), command, output=main_output)
        time.sleep(0.1)
        return run_command(local_root, command, env_var, pipeto, retry - 1)
    return main_output