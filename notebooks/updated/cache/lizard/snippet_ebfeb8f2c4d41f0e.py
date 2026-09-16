def LCM(input_dim, num_outputs, kernels_list, W_rank=1, name='ICM'):
    Nk = len(kernels_list)
    K = ICM(input_dim, num_outputs, kernels_list[0], W_rank, name='%s%s' %
        (name, 0))
    j = 1
    for kernel in kernels_list[1:]:
        K += ICM(input_dim, num_outputs, kernel, W_rank, name='%s%s' % (
            name, j))
        j += 1
    return K