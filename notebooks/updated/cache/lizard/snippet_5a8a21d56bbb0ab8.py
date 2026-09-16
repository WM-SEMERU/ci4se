def initialize():
    dst_path = get_user_config_path()
    copied = False
    if not os.path.exists(dst_path):
        src_path = os.path.join(os.path.dirname(__file__), 'defaultconfig.py')
        shutil.copyfile(src_path, dst_path)
        copied = True
    return copied, dst_path