def module(command, *args):
    if 'MODULESHOME' not in os.environ:
        print('payu: warning: No Environment Modules found; skipping {0} call.'
            .format(command))
        return
    modulecmd = '{0}/bin/modulecmd'.format(os.environ['MODULESHOME'])
    cmd = '{0} python {1} {2}'.format(modulecmd, command, ' '.join(args))
    envs, _ = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE
        ).communicate()
    exec(envs)