def check_for_wdiff():
    cmd = ['which', CMD_WDIFF]
    DEVNULL = open(os.devnull, 'wb')
    proc = sub.Popen(cmd, stdout=DEVNULL)
    proc.wait()
    DEVNULL.close()
    if proc.returncode != 0:
        msg = "the `{}` command can't be found".format(CMD_WDIFF)
        raise WdiffNotFoundError(msg)