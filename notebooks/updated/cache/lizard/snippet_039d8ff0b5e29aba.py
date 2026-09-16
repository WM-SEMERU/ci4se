def prepare(cls, options, round_manager):
    super(RunJvmPrepCommandBase, cls).prepare(options, round_manager)
    round_manager.require_data('compile_classpath')
    if not cls.classpath_product_only:
        round_manager.require_data('runtime_classpath')