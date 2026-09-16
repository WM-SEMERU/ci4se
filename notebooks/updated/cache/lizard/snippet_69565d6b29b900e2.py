def get_all_as_list(self, dir='_todo_dir'):
    dir = getattr(self, dir)
    list = [x for x in os.listdir(dir) if x.endswith('.json') or x.endswith
        ('.json.gz')]
    full = [os.path.join(dir, x) for x in list]
    full.sort(key=lambda x: os.path.getmtime(x))
    return full