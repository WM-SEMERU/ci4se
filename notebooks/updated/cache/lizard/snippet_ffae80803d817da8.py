def _get_runner(classpath, main, jvm_options, args, executor, cwd,
    distribution, create_synthetic_jar, synthetic_jar_dir):
    executor = executor or SubprocessExecutor(distribution)
    safe_cp = classpath
    if create_synthetic_jar:
        safe_cp = safe_classpath(classpath, synthetic_jar_dir)
        logger.debug('Bundling classpath {} into {}'.format(':'.join(
            classpath), safe_cp))
    return executor.runner(safe_cp, main, args=args, jvm_options=
        jvm_options, cwd=cwd)