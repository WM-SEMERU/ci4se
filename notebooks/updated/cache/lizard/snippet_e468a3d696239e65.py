def disc_benchmarks(root, ignore_import_errors=False):
    root_name = os.path.basename(root)
    for module in disc_modules(root_name, ignore_import_errors=
        ignore_import_errors):
        for attr_name, module_attr in ((k, v) for k, v in module.__dict__.
            items() if not k.startswith('_')):
            if inspect.isclass(module_attr):
                for name, class_attr in inspect.getmembers(module_attr):
                    if inspect.isfunction(class_attr) or inspect.ismethod(
                        class_attr):
                        benchmark = _get_benchmark(name, module,
                            module_attr, class_attr)
                        if benchmark is not None:
                            yield benchmark
            elif inspect.isfunction(module_attr):
                benchmark = _get_benchmark(attr_name, module, None, module_attr
                    )
                if benchmark is not None:
                    yield benchmark