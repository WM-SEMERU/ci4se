def __update_siblings_active_labels_states(self, active_label):
    LOGGER.debug("> Clicked 'Active_QLabel': '{0}'.".format(active_label))
    for item in self.__active_labels:
        if item is active_label:
            continue
        umbra.ui.common.signals_blocker(item, item.set_checked, False)