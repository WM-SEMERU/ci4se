def warnify(self, message, duration=3000, notification_clicked_slot=None,
    **kwargs):
    return self.notify(message, duration, notification_clicked_slot,
        message_level='Warning', color=QColor(220, 128, 64),
        background_color=QColor(32, 32, 32), border_color=QColor(220, 128, 
        64), **kwargs)