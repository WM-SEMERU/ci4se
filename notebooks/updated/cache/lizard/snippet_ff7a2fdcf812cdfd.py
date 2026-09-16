def get_layouts_active_labels(self):
    self.__layouts_active_labels_collection = Active_QLabelsCollection(self)
    self.__layouts_active_labels_collection.add_active_label(self.
        get_layout_active_label((UiConstants.development_icon, UiConstants.
        development_hover_icon, UiConstants.development_active_icon),
        'Development_active_label', 'Development', 'development_centric',
        Qt.Key_9))
    self.__layouts_active_labels_collection.add_active_label(self.
        get_layout_active_label((UiConstants.preferences_icon, UiConstants.
        preferences_hover_icon, UiConstants.preferences_active_icon),
        'Preferences_active_label', 'Preferences', 'preferences_centric',
        Qt.Key_0))
    return self.__layouts_active_labels_collection.active_labels