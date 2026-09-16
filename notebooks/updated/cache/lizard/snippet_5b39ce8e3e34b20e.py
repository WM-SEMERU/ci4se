def main(*args):
    try:
        subprocess.check_call([sys.executable, '-m', 'pip'] + list(args))
        return 0
    except subprocess.CalledProcessError as err:
        return err.returncode