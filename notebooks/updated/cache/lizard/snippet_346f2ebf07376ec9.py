def checkerboard_matrix_filtering(similarity_matrix, kernel_width, peak_range):
    checkerboard_matrix = get_checkerboard_matrix(kernel_width)
    d = []
    for i in range(0, similarity_matrix.shape[0] - 2 * kernel_width):
        base = similarity_matrix[i:i + kernel_width * 2, i:i + kernel_width * 2
            ]
        d.append(np.sum(np.multiply(base, checkerboard_matrix)))
    top_left_d = []
    for i in range(0, kernel_width):
        base = similarity_matrix[0:i + kernel_width, 0:i + kernel_width]
        top_left_d.append(np.sum(np.multiply(base, checkerboard_matrix[
            kernel_width - i:, kernel_width - i:])))
    convolution_values = top_left_d + d + [(0) for i in range(0, kernel_width)]
    peaks = find_peaks_cwt(convolution_values, np.arange(1, peak_range))
    peaks = [0] + peaks + [len(convolution_values) - 1]
    return peaks, convolution_values