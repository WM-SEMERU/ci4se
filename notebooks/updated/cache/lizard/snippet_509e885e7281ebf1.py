def remove_jobdir_if_not_resume(self):
    jobdir = self.__scrapy_options['JOBDIR']
    if (not self.shall_resume or self.daemonize) and os.path.exists(jobdir):
        shutil.rmtree(jobdir)
        self.log.info('Removed ' + jobdir +
            " since '--resume' was not passed to initial.py or this crawler was daemonized."
            )