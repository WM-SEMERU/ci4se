def _prepare_executor(self, data, executor):
    logger.debug(__('Preparing executor for Data with id {}', data.id))
    import resolwe.flow.executors as executor_package
    exec_dir = os.path.dirname(inspect.getsourcefile(executor_package))
    dest_dir = self._get_per_data_dir('RUNTIME_DIR', data.location.subpath)
    dest_package_dir = os.path.join(dest_dir, 'executors')
    shutil.copytree(exec_dir, dest_package_dir)
    dir_mode = self.settings_actual.get('FLOW_EXECUTOR', {}).get(
        'RUNTIME_DIR_MODE', 493)
    os.chmod(dest_dir, dir_mode)
    class_name = executor.rpartition('.executors.')[-1]
    return '.{}'.format(class_name), dest_dir