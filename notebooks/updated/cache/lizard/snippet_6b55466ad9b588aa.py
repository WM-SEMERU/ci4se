def save_frames(obj, filename, fmt=None, backend=None, options=None):
    backend = Store.current_backend if backend is None else backend
    renderer = Store.renderers[backend]
    fmt = renderer.params('fig').objects[0] if fmt is None else fmt
    plot = renderer.get_plot(obj)
    for i in range(len(plot)):
        plot.update(i)
        renderer.save(plot, '%s_%s' % (filename, i), fmt=fmt, options=options)