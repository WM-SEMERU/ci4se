def variable_summaries(vars_, groups=None, scope='weights'):
    groups = groups or {'all': '.*'}
    grouped = collections.defaultdict(list)
    for var in vars_:
        for name, pattern in groups.items():
            if re.match(pattern, var.name):
                name = re.sub(pattern, name, var.name)
                grouped[name].append(var)
    for name in groups:
        if name not in grouped:
            tf.logging.warn("No variables matching '{}' group.".format(name))
    summaries = []
    for name, vars_ in grouped.items():
        vars_ = [tf.reshape(var, [-1]) for var in vars_]
        vars_ = tf.concat(vars_, 0)
        summaries.append(tf.summary.histogram(scope + '/' + name, vars_))
    return tf.summary.merge(summaries)