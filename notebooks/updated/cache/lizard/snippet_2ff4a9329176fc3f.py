def compute_y(self, coefficients, num_x):
    y_vals = []
    for x in range(1, num_x + 1):
        y = sum([(c * x ** i) for i, c in enumerate(coefficients[::-1])])
        y_vals.append(y)
    return y_vals