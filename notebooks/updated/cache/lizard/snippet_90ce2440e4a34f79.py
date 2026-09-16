def sysctl(command):
    out = subprocess.check_output(command)
    result = out.split(b' ')[1]
    try:
        return int(result)
    except ValueError:
        return result