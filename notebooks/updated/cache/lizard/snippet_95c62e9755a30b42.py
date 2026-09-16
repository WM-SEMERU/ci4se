def linear_interpolate(x_axis, y_axis, x_new_axis, enable_warning=True):
    left_pad_x, left_pad_y = list(), list()
    right_pad_x, right_pad_y = list(), list()
    if x_new_axis[0] < x_axis[0]:
        if enable_warning:
            print(
                'WARNING! the first element of x_new_axis is at left of x_axis. Use linear_interpolate(enable_warning=False) to disable this warning.'
                )
        left_pad_x.append(x_new_axis[0])
        left_pad_y.append(locate(x_axis[0], y_axis[0], x_axis[1], y_axis[1],
            x_new_axis[0]))
    if x_new_axis[-1] > x_axis[-1]:
        if enable_warning:
            print(
                'WARNING! the last element of x_new_axis is at right of x_axis. Use linear_interpolate(enable_warning=False) to disable this warning.'
                )
        right_pad_x.append(x_new_axis[-1])
        right_pad_y.append(locate(x_axis[-1], y_axis[-1], x_axis[-2],
            y_axis[-2], x_new_axis[-1]))
    if not (len(left_pad_x) == 0 and len(right_pad_x) == 0):
        x_axis = left_pad_x + x_axis + right_pad_x
        y_axis = left_pad_y + y_axis + right_pad_y
    return rigid_linear_interpolate(x_axis, y_axis, x_new_axis)