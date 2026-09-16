def _report_profile(self, command, lock_name, elapsed_time, memory):
    message_raw = str(command) + '\t ' + str(lock_name) + '\t' + str(datetime
        .timedelta(seconds=round(elapsed_time, 2))) + '\t ' + str(memory)
    with open(self.pipeline_profile_file, 'a') as myfile:
        myfile.write(message_raw + '\n')