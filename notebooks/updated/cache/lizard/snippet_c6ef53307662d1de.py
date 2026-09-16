def default_tasks(self):
    return dict((name, Task(action=name, label='Harpoon')) for name in
        default_actions)