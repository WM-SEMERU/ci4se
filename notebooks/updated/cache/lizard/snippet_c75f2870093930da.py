def save_img(self, file_name=None, file_type='gif', mode='dot'):
    if not file_name:
        warnings.warn(DeprecationWarning, 'always pass a file_name')
        file_name = 'out'
    if mode == 'neato':
        self.save_dot(self.temp_neo)
        neato_cmd = '%s -o %s %s' % (self.neato, self.temp_dot, self.temp_neo)
        os.system(neato_cmd)
        plot_cmd = self.dot
    else:
        self.save_dot(self.temp_dot)
        plot_cmd = self.dot
    file_name = '%s.%s' % (file_name, file_type)
    create_cmd = '%s -T%s %s -o %s' % (plot_cmd, file_type, self.temp_dot,
        file_name)
    os.system(create_cmd)