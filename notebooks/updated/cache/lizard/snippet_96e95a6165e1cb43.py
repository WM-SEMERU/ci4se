def get_examples(examples_dir='examples/'):
    all_files = os.listdir(examples_dir)
    python_files = [f for f in all_files if is_python_file(f)]
    basenames = [remove_suffix(f) for f in python_files]
    modules = [import_module(module) for module in pathify(basenames)]
    return [module for module in modules if getattr(module, 'app', None) is not
        None]