def cutout_source(x_pos, y_pos, image, kernelsize, shift=True):
    if kernelsize % 2 == 0:
        raise ValueError('even pixel number kernel size not supported!')
    x_int = int(round(x_pos))
    y_int = int(round(y_pos))
    n = len(image)
    d = (kernelsize - 1) / 2
    x_max = int(np.minimum(x_int + d + 1, n))
    x_min = int(np.maximum(x_int - d, 0))
    y_max = int(np.minimum(y_int + d + 1, n))
    y_min = int(np.maximum(y_int - d, 0))
    image_cut = copy.deepcopy(image[y_min:y_max, x_min:x_max])
    shift_x = x_int - x_pos
    shift_y = y_int - y_pos
    if shift is True:
        kernel_shift = de_shift_kernel(image_cut, shift_x, shift_y,
            iterations=50)
    else:
        kernel_shift = image_cut
    kernel_final = np.zeros((kernelsize, kernelsize))
    k_l2_x = int((kernelsize - 1) / 2)
    k_l2_y = int((kernelsize - 1) / 2)
    xk_min = np.maximum(0, -x_int + k_l2_x)
    yk_min = np.maximum(0, -y_int + k_l2_y)
    xk_max = np.minimum(kernelsize, -x_int + k_l2_x + n)
    yk_max = np.minimum(kernelsize, -y_int + k_l2_y + n)
    kernel_final[yk_min:yk_max, xk_min:xk_max] = kernel_shift
    return kernel_final