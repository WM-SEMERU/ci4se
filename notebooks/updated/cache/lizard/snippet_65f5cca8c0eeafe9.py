def _execute(self, workdir, with_mpirun=False, exec_args=None):
    qadapter = self.manager.qadapter
    if not with_mpirun:
        qadapter.name = None
    if self.verbose:
        print('Working in:', workdir)
    script = qadapter.get_script_str(job_name=self.name, launch_dir=workdir,
        executable=self.executable, qout_path='qout_file.path', qerr_path=
        'qerr_file.path', stdin=self.stdin_fname, stdout=self.stdout_fname,
        stderr=self.stderr_fname, exec_args=exec_args)
    script_file = os.path.join(workdir, 'run' + self.name + '.sh')
    with open(script_file, 'w') as fh:
        fh.write(script)
        os.chmod(script_file, 480)
    qjob, process = qadapter.submit_to_queue(script_file)
    self.stdout_data, self.stderr_data = process.communicate()
    self.returncode = process.returncode
    return self.returncode