def create_script_for_location(content, destination):
    temp = tempfile.NamedTemporaryFile(mode='w', delete=False)
    temp.write(content)
    temp.close()
    shutil.move(temp.name, destination)
    cur_perms = os.stat(destination).st_mode
    set_perms = cur_perms | stat.S_IXOTH | stat.S_IXGRP | stat.S_IXUSR
    os.chmod(destination, set_perms)