def plot_temp_diagrams(config, results, temp_dir):
    display_name = {'time': 'Compilation time (s)', 'memory':
        'Compiler memory usage (MB)'}
    files = config['files']
    img_files = []
    if any('slt' in result for result in results) and 'bmp' in files.values()[0
        ]:
        config['modes']['slt'
            ] = 'Using BOOST_METAPARSE_STRING with string literal templates'
        for f in files.values():
            f['slt'] = f['bmp'].replace('bmp', 'slt')
    for measured in ['time', 'memory']:
        mpts = sorted(int(k) for k in files.keys())
        img_files.append(os.path.join(temp_dir, '_{0}.png'.format(measured)))
        plot({m: [(x, results[files[str(x)][m]][measured]) for x in mpts] for
            m in config['modes'].keys()}, config['modes'], display_name[
            measured], (config['x_axis_label'], display_name[measured]),
            img_files[-1])
    return img_files