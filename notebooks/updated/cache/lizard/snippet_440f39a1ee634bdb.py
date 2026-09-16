def install_alternative(name, target, source, priority=50):
    if os.path.exists(target) and not os.path.islink(target):
        shutil.move(target, '{}.bak'.format(target))
    cmd = ['update-alternatives', '--force', '--install', target, name,
        source, str(priority)]
    subprocess.check_call(cmd)