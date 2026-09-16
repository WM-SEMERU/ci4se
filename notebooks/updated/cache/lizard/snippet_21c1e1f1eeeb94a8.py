def thread_exception(self, raised_exception):
    print('Thread execution was stopped by the exception. Exception: %s' %
        str(raised_exception))
    print('Traceback:')
    print(traceback.format_exc())