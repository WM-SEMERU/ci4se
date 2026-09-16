def stop(self):
    self.active_thread = False
    if self.thread_push_instance and self.thread_push_instance.isAlive():
        self.thread_push_instance.join()
    with self.batch_commit('STREAM_END'):
        for path, handle in six.iteritems(self.streamed_files.copy()):
            full_path = os.path.normpath(self.temp_path + '/stream-blob/' +
                self.job_id + '/' + path)
            self.logger.debug('Git stream end for file: ' + full_path)
            del self.streamed_files[path]
            try:
                self.stream_files_lock.acquire()
                if not handle.closed:
                    handle.flush()
                    handle.close()
            finally:
                self.stream_files_lock.release()
            with open(full_path, 'r') as f:
                self.commit_file(path, path, f.read())
            if not self.keep_stream_files:
                os.unlink(full_path)
    with self.batch_commit('STORE_END'):
        for path, bar in six.iteritems(self.store_files.copy()):
            full_path = os.path.normpath(self.temp_path + '/store-blob/' +
                self.job_id + '/' + path)
            self.logger.debug('Git store end for file: ' + full_path)
            del self.store_files[path]
            try:
                self.stream_files_lock.acquire()
                self.commit_file(path, path, open(full_path, 'r').read())
            finally:
                self.stream_files_lock.release()
            if not self.keep_stream_files:
                os.unlink(full_path)