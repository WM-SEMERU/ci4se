def colorbar(self, mappable=None, cax=None, ax=None, fraction=0.0, label=
    None, emit=True, **kwargs):
    mappable, kwargs = gcbar.process_colorbar_kwargs(self, mappable, ax,
        cax=cax, fraction=fraction, **kwargs)
    cbar = super(Plot, self).colorbar(mappable, **kwargs)
    self.colorbars.append(cbar)
    if label:
        cbar.set_label(label)
    if emit:
        ax = kwargs.pop('ax')
        norm = mappable.norm
        cmap = mappable.get_cmap()
        for map_ in (ax.collections + ax.images):
            map_.set_norm(norm)
            map_.set_cmap(cmap)
    return cbar