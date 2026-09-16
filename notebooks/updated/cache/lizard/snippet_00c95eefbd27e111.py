def stop_pipeline(self, status=COMPLETE_FLAG):
    self._set_status_flag(status)
    self._cleanup()
    self.report_result('Time', str(datetime.timedelta(seconds=self.
        time_elapsed(self.starttime))))
    self.report_result('Success', time.strftime('%m-%d-%H:%M:%S'))
    print('\n##### [Epilogue:]')
    print('* ' + 'Total elapsed time'.rjust(20) + ':  ' + str(datetime.
        timedelta(seconds=self.time_elapsed(self.starttime))))
    print('* ' + 'Peak memory used'.rjust(20) + ':  ' + str(round(self.
        peak_memory, 2)) + ' GB')
    if self.halted:
        return
    self.timestamp('* Pipeline completed at: '.rjust(20))