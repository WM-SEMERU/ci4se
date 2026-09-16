def _handle_job_set(function):

    def call(self, job_set=taskhandle.NullJobSet()):
        job_set.started_job(str(self))
        function(self)
        job_set.finished_job()
    return call