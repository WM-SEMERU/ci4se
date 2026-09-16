def _set_cpu_throttling(self):
    if not self.is_running():
        return
    try:
        if sys.platform.startswith('win') and hasattr(sys, 'frozen'):
            cpulimit_exec = os.path.join(os.path.dirname(os.path.abspath(
                sys.executable)), 'cpulimit', 'cpulimit.exe')
        else:
            cpulimit_exec = 'cpulimit'
        subprocess.Popen([cpulimit_exec, '--lazy', '--pid={}'.format(self.
            _process.pid), '--limit={}'.format(self._cpu_throttling)], cwd=
            self.working_dir)
        log.info('CPU throttled to {}%'.format(self._cpu_throttling))
    except FileNotFoundError:
        raise QemuError(
            'cpulimit could not be found, please install it or deactivate CPU throttling'
            )
    except (OSError, subprocess.SubprocessError) as e:
        raise QemuError('Could not throttle CPU: {}'.format(e))