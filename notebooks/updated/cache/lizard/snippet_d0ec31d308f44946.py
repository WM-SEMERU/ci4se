def run_command_orig(cmd):
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if process.returncode == 0:
        os.killpg(os.getpgid(pro.pid), signal.SIGTERM)
    else:
        raise BadRCError("Bad rc (%s) for cmd '%s': %s" % (process.
            returncode, cmd, stdout + stderr))
    return stdout