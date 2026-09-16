def getXMLDescription(cliExecutable, **kwargs):
    command = [cliExecutable, '--xml']
    stdout, stdoutFilename = tempfile.mkstemp('.stdout')
    stderr, stderrFilename = tempfile.mkstemp('.stderr')
    try:
        p = popenCLIExecutable(command, stdout=stdout, stderr=stderr, **kwargs)
        ec = p.wait()
        with open(stderrFilename) as f:
            for line in f:
                logger.warning('%s: %s' % (os.path.basename(cliExecutable),
                    line[:-1]))
        if ec:
            raise RuntimeError('Calling %s failed (exit code %d)' % (
                cliExecutable, ec))
        with open(stdoutFilename) as f:
            return ET.parse(f)
    finally:
        os.close(stdout)
        os.close(stderr)
        os.unlink(stdoutFilename)
        os.unlink(stderrFilename)