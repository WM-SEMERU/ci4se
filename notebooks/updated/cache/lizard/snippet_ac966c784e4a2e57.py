def _load_controllers(self):
    for file_name in os.listdir(os.path.join(self._project_dir, 'controllers')
        ):
        if not file_name.startswith('_'):
            module_name = file_name.split('.', 1)[0]
            module_path = 'controllers.{}'.format(module_name)
            module = import_module(module_path)
            controller_class_name = module_name.title().replace('_', '')
            controller_class = getattr(module, controller_class_name)
            controller = controller_class()
            for action_name in dir(controller):
                action = getattr(controller, action_name)
                if action_name.startswith('_') or not callable(action):
                    continue
                url_path = '/'.join([module_name, action_name])
                self._controllers[url_path] = action
    return self._controllers