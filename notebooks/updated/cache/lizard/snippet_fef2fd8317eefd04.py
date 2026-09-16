def call(self, module, *args, **kwargs):
    module = self._resolver.load_module(module)
    if not hasattr(module, 'main'):
        raise CommandExecutionError(
            'This module is not callable (see "ansible.help {0}")'.format(
            module.__name__.replace('ansible.modules.', '')))
    if args:
        kwargs['_raw_params'] = ' '.join(args)
    js_args = str('{{"ANSIBLE_MODULE_ARGS": {args}}}')
    js_args = js_args.format(args=salt.utils.json.dumps(kwargs))
    proc_out = salt.utils.timed_subprocess.TimedProc(['echo', '{0}'.format(
        js_args)], stdout=subprocess.PIPE, timeout=self.timeout)
    proc_out.run()
    proc_exc = salt.utils.timed_subprocess.TimedProc(['python', module.
        __file__], stdin=proc_out.stdout, stdout=subprocess.PIPE, timeout=
        self.timeout)
    proc_exc.run()
    try:
        out = salt.utils.json.loads(proc_exc.stdout)
    except ValueError as ex:
        out = {'Error': proc_exc.stderr and proc_exc.stderr + '.' or six.
            text_type(ex)}
        if proc_exc.stdout:
            out['Given JSON output'] = proc_exc.stdout
        return out
    if 'invocation' in out:
        del out['invocation']
    out['timeout'] = self.timeout
    return out