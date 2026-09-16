def _RunSingleHook(self, hook_cls, executed_set, required=None):
    if hook_cls in executed_set:
        return
    for pre_hook in hook_cls.pre:
        self._RunSingleHook(pre_hook, executed_set, required=hook_cls.__name__)
    cls_instance = hook_cls()
    if required:
        logging.debug('Initializing %s, required by %s', hook_cls.__name__,
            required)
    else:
        logging.debug('Initializing %s', hook_cls.__name__)
    cls_instance.Run()
    executed_set.add(hook_cls)
    if hook_cls not in self.already_run_once:
        cls_instance.RunOnce()
        self.already_run_once.add(hook_cls)