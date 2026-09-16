def sexec(context, command, error_on_nonzero=True):
    import six
    if isinstance(context, six.string_types):
        E = environ(context)
    else:
        E = context
    try:
        logger.debug("Executing: '%s'", ' '.join(command))
        p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=
            subprocess.STDOUT, env=E)
        stdout, stderr = p.communicate()
        if p.returncode != 0:
            if error_on_nonzero:
                raise RuntimeError(
                    "Execution of '%s' exited with status != 0 (%d): %s" %
                    (' '.join(command), p.returncode, str_(stdout)))
            else:
                logger.debug(
                    "Execution of '%s' exited with status != 0 (%d): %s" %
                    (' '.join(command), p.returncode, str_(stdout)))
        return stdout.strip()
    except KeyboardInterrupt:
        os.kill(p.pid, signal.SIGTERM)
        sys.exit(signal.SIGTERM)