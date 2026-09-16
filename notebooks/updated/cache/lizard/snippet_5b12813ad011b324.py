def get_kernel_message(self, timeout=None, stream='iopub'):
    return self.kernel.get_message(stream, timeout=timeout)