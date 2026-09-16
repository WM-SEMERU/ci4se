def compute_classpath(cls, targets, classpath_products,
    extra_classpath_tuples, confs):
    return list(entry.path for entry in cls.compute_classpath_entries(
        targets, classpath_products, ((scope, ClasspathEntry(path)) for 
        scope, path in extra_classpath_tuples), confs))