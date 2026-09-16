def to_dict(self):
    task_desc_as_dict = {'uid': self._uid, 'name': self._name, 'state':
        self._state, 'state_history': self._state_history, 'pre_exec': self
        ._pre_exec, 'executable': self._executable, 'arguments': self.
        _arguments, 'post_exec': self._post_exec, 'cpu_reqs': self.
        _cpu_reqs, 'gpu_reqs': self._gpu_reqs, 'lfs_per_process': self.
        _lfs_per_process, 'upload_input_data': self._upload_input_data,
        'copy_input_data': self._copy_input_data, 'link_input_data': self.
        _link_input_data, 'move_input_data': self._move_input_data,
        'copy_output_data': self._copy_output_data, 'move_output_data':
        self._move_output_data, 'download_output_data': self.
        _download_output_data, 'stdout': self._stdout, 'stderr': self.
        _stderr, 'exit_code': self._exit_code, 'path': self._path, 'tag':
        self._tag, 'parent_stage': self._p_stage, 'parent_pipeline': self.
        _p_pipeline}
    return task_desc_as_dict