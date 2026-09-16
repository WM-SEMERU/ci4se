def init_nvidia(self):
    if import_error_tag:
        self.nvml_ready = False
    try:
        pynvml.nvmlInit()
        self.device_handles = get_device_handles()
        self.nvml_ready = True
    except Exception:
        logger.debug('pynvml could not be initialized.')
        self.nvml_ready = False
    return self.nvml_ready