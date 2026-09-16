def resume_processes(self, as_group, scaling_processes=None):
    params = {'AutoScalingGroupName': as_group}
    if scaling_processes:
        self.build_list_params(params, scaling_processes, 'ScalingProcesses')
    return self.get_status('ResumeProcesses', params)