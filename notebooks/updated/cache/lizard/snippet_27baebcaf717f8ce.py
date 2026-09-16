def detect_language(lang, kernel_source):
    if lang is None:
        if callable(kernel_source):
            raise TypeError(
                'Please specify language when using a code generator function')
        kernel_string = get_kernel_string(kernel_source)
        if '__global__' in kernel_string:
            lang = 'CUDA'
        elif '__kernel' in kernel_string:
            lang = 'OpenCL'
        else:
            lang = 'C'
    return lang