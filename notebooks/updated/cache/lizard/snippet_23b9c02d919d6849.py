def locate_resource(name, lang, filter=None):
    task_dir = resource_dir.get(name, name)
    package_id = '{}.{}'.format(task_dir, lang)
    p = path.join(polyglot_path, task_dir, lang)
    if not path.isdir(p):
        if downloader.status(package_id) != downloader.INSTALLED:
            raise ValueError(
                """This resource is available in the index but not downloaded, yet. Try to run

polyglot download {}"""
                .format(package_id))
    return path.join(p, os.listdir(p)[0])