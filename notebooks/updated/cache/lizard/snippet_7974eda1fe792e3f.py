def set_nvidia_environment_variables(environment, gpu_ids):
    if gpu_ids:
        nvidia_visible_devices = ''
        for gpu_id in gpu_ids:
            nvidia_visible_devices += '{},'.format(gpu_id)
        environment['NVIDIA_VISIBLE_DEVICES'] = nvidia_visible_devices