def interactive_output(f, controls):
    out = Output()

    def observer(change):
        kwargs = {k: v.value for k, v in controls.items()}
        show_inline_matplotlib_plots()
        with out:
            clear_output(wait=True)
            f(**kwargs)
            show_inline_matplotlib_plots()
    for k, w in controls.items():
        w.observe(observer, 'value')
    show_inline_matplotlib_plots()
    observer(None)
    return out