def get_task(config):
    path = os.path.join(config['work_dir'], 'task.json')
    message = "Can't read task from {}!\n%(exc)s".format(path)
    contents = load_json_or_yaml(path, is_path=True, message=message)
    return contents