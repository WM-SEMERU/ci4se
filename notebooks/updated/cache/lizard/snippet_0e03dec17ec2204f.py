def run(self, interpreter):
    with utils.ChangeDir(self.dirname):
        command_list = ['PYTHONPATH=' + main_dir, interpreter, self.filename
            ] + list(self.args)
        try:
            proc = Popen(' '.join(command_list), stdout=PIPE, stderr=PIPE,
                shell=True)
            stream_data = proc.communicate()
        except Exception as e:
            logger.error('Error {0} while executing extract_dist command.'.
                format(e))
            raise ExtractionError
        stream_data = [utils.console_to_str(s) for s in stream_data]
        if proc.returncode:
            logger.error('Subprocess failed, stdout: {0[0]}, stderr: {0[1]}'
                .format(stream_data))
        self._result = json.loads(stream_data[0].split(
            'extracted json data:\n')[-1].split('\n')[0])