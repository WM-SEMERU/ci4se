def _get_config_name():
    p = subprocess.Popen('git config --get user.name', shell=True, stdout=
        subprocess.PIPE, stderr=subprocess.STDOUT)
    output = p.stdout.readlines()
    return _stripslashes(output[0])