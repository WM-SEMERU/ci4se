def load_executor(self, executor_name):
    executor_name = executor_name + '.prepare'
    module = import_module(executor_name)
    return module.FlowExecutorPreparer()