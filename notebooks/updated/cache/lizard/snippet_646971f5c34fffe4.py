def widgetSubCheckBoxRect(widget, option):
    opt = QtWidgets.QStyleOption()
    opt.initFrom(widget)
    style = widget.style()
    return style.subElementRect(QtWidgets.QStyle.SE_ViewItemCheckIndicator,
        opt, widget)