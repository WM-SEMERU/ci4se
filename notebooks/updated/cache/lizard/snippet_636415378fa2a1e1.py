def show_focus_indicator(viewer, tf, color='white'):
    tag = '_$focus_indicator'
    canvas = viewer.get_private_canvas()
    try:
        fcsi = canvas.get_object_by_tag(tag)
        if not tf:
            canvas.delete_object_by_tag(tag)
        else:
            fcsi.color = color
    except KeyError:
        if tf:
            Fcsi = canvas.get_draw_class('focusindicator')
            fcsi = Fcsi(color=color)
            canvas.add(fcsi, tag=tag, redraw=False)
            viewer.add_callback('focus', fcsi.focus_cb)
    canvas.update_canvas(whence=3)