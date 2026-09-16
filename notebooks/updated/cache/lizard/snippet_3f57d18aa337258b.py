def calc_ifft_with_PyCUDA(Signalfft):
    print('starting ifft')
    Signalfft = Signalfft.astype(_np.complex64)
    Signalfft_gpu = _gpuarray.to_gpu(Signalfft[0:len(Signalfft) // 2 + 1])
    Signal_gpu = _gpuarray.empty(len(Signalfft), _np.float32)
    plan = _Plan(len(Signalfft), _np.complex64, _np.float32)
    _ifft(Signalfft_gpu, Signal_gpu, plan)
    Signal = Signal_gpu.get() / (2 * len(Signalfft))
    print('ifft done')
    return Signal