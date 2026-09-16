def tail(filepath='log.txt', lines=50):
    try:
        filepath = os.path.expanduser(os.path.expandvars(filepath))
        if os.path.isfile(filepath):
            text = subprocess.check_output(['tail', '-' + str(lines), filepath]
                )
            if text:
                return text
            else:
                return False
        else:
            return False
    except:
        return False