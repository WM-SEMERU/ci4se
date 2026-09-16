def _contour_data(data, length_scales, log_SNRs, kernel_call=GPy.kern.RBF):
    lls = []
    total_var = np.var(data['Y'])
    kernel = kernel_call(1, variance=1.0, lengthscale=1.0)
    model = GPy.models.GPRegression(data['X'], data['Y'], kernel=kernel)
    for log_SNR in log_SNRs:
        SNR = 10.0 ** log_SNR
        noise_var = total_var / (1.0 + SNR)
        signal_var = total_var - noise_var
        model.kern['.*variance'] = signal_var
        model.likelihood.variance = noise_var
        length_scale_lls = []
        for length_scale in length_scales:
            model['.*lengthscale'] = length_scale
            length_scale_lls.append(model.log_likelihood())
        lls.append(length_scale_lls)
    return np.array(lls)