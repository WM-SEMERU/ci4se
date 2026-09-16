def show_pushable(collector, **kwargs):
    collector.configuration['harpoon'].only_pushable = True
    show(collector, **kwargs)