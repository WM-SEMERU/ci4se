def update_display(self, iteration, disp_level, col_width=12):
    if disp_level == 0:
        return
    else:
        if disp_level == 1 and iteration >= 0:
            print('[Iteration %i]' % iteration)
        if disp_level > 1:
            data = valmap(last, self.metadata)
            keys = ['Time (s)', 'Primal resid', 'Dual resid', 'rho']
            if iteration == 1:
                print(tableprint.header(keys, width=col_width))
            print(tableprint.row([data[k] for k in keys], width=col_width,
                format_spec='4g'))
            if iteration == -1:
                print(tableprint.bottom(len(keys), width=col_width) + '\n')
        if iteration == -1 and self.converged:
            print('Converged after %i iterations!' % len(self.metadata[
                'Primal resid']))