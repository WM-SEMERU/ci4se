def task(func, *args, **kwargs):
    prefix = '\n# '
    tail = '\n'
    return fabric.api.task(print_full_name(color=magenta, prefix=prefix,
        tail=tail)(print_doc1(func)), *args, **kwargs)