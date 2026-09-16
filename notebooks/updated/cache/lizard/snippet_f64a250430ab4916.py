def display_warning_message_bar(title=None, message=None, more_details=None,
    button_text=tr('Show details ...'), duration=8, iface_object=iface):
    iface_object.messageBar().clearWidgets()
    widget = iface_object.messageBar().createMessage(title, message)
    if more_details:
        button = QPushButton(widget)
        button.setText(button_text)
        button.pressed.connect(lambda : display_warning_message_box(title=
            title, message=more_details))
        widget.layout().addWidget(button)
    iface_object.messageBar().pushWidget(widget, Qgis.Warning, duration)