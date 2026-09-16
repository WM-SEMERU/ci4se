def Engauge_2d_parser(lines, flat=False):
    z_values = []
    x_lists = []
    y_lists = []
    working_xs = []
    working_ys = []
    new_curve = True
    for line in lines:
        if line.strip() == '':
            new_curve = True
        elif new_curve:
            z = float(line.split(',')[1])
            z_values.append(z)
            if working_xs and working_ys:
                x_lists.append(working_xs)
                y_lists.append(working_ys)
            working_xs = []
            working_ys = []
            new_curve = False
        else:
            x, y = [float(i) for i in line.strip().split(',')]
            working_xs.append(x)
            working_ys.append(y)
    x_lists.append(working_xs)
    y_lists.append(working_ys)
    if flat:
        all_zs = []
        all_xs = []
        all_ys = []
        for z, xs, ys in zip(z_values, x_lists, y_lists):
            for x, y in zip(xs, ys):
                all_zs.append(z)
                all_xs.append(x)
                all_ys.append(y)
        return all_zs, all_xs, all_ys
    return z_values, x_lists, y_lists