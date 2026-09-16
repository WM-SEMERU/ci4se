def _execute(self, args, log=True):
    if not self._ready:
        self.open_or_create()
    output = ''
    error = ''
    try:
        proc = subprocess.Popen(args, cwd=self.path, env=self.env, stdout=
            subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = proc.communicate()
        returncode = proc.returncode
        if returncode:
            raise subprocess.CalledProcessError(returncode, proc, (output,
                error))
        return to_text(output)
    except OSError as e:
        prog = args[0]
        if prog[0] != os.sep:
            prog = os.path.join(self.path, prog)
        raise OSError('%s: %s' % (prog, six.u(str(e))))
    except subprocess.CalledProcessError as e:
        output, error = e.output
        e.output = output
        raise e
    finally:
        if log:
            try:
                self._write_to_log(to_text(output))
                self._write_to_error(to_text(error))
            except NameError:
                pass