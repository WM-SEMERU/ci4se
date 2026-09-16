def get_script(script_name):
    install_dir = get_installdir()
    script_path = '%s/build/scripts/%s' % (install_dir, script_name)
    if os.path.exists(script_path):
        return script_path
    else:
        bot.error('Script %s is not included in singularity-python!' %
            script_path)
        return None