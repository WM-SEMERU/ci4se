def resume():
    if not settings.platformCompatible():
        return False
    output, error = subprocess.Popen(['osascript', '-e', RESUME], stdout=
        subprocess.PIPE).communicate()