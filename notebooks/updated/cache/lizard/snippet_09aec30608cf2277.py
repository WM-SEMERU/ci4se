def get_data_times_for_job_workflow(self, num_job):
    shift_dur = self.curr_seg[0] + int(self.job_time_shift * num_job + 0.0001)
    job_data_seg = self.data_chunk.shift(shift_dur)
    return job_data_seg