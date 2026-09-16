def action_create(self, courseid, taskid, path):
    path = path.strip()
    if not path.startswith('/'):
        path = '/' + path
    want_directory = path.endswith('/')
    wanted_path = self.verify_path(courseid, taskid, path, True)
    if wanted_path is None:
        return self.show_tab_file(courseid, taskid, _('Invalid new path'))
    task_fs = self.task_factory.get_task_fs(courseid, taskid)
    if want_directory:
        task_fs.from_subfolder(wanted_path).ensure_exists()
    else:
        task_fs.put(wanted_path, b'')
    return self.show_tab_file(courseid, taskid)