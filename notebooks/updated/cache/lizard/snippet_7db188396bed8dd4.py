def addIcon(iconActor, pos=3, size=0.08):
    vp = settings.plotter_instance
    if not vp.renderer:
        colors.printc(
            '~lightningWarning: Use addIcon() after first rendering the scene.'
            , c=3)
        save_int = vp.interactive
        vp.show(interactive=0)
        vp.interactive = save_int
    widget = vtk.vtkOrientationMarkerWidget()
    widget.SetOrientationMarker(iconActor)
    widget.SetInteractor(vp.interactor)
    if utils.isSequence(pos):
        widget.SetViewport(pos[0] - size, pos[1] - size, pos[0] + size, pos
            [1] + size)
    elif pos < 2:
        widget.SetViewport(0, 1 - 2 * size, size * 2, 1)
    elif pos == 2:
        widget.SetViewport(1 - 2 * size, 1 - 2 * size, 1, 1)
    elif pos == 3:
        widget.SetViewport(0, 0, size * 2, size * 2)
    elif pos == 4:
        widget.SetViewport(1 - 2 * size, 0, 1, size * 2)
    widget.EnabledOn()
    widget.InteractiveOff()
    vp.widgets.append(widget)
    if iconActor in vp.actors:
        vp.actors.remove(iconActor)
    return widget