def connect_data_item_reference(self, data_item_reference):
    display_item = data_item_reference.display_item
    data_item = display_item.data_item if display_item else None
    if data_item and display_item:
        self.__connect_display(display_item)
    else:

        def data_item_reference_changed():
            self.__data_item_reference_changed_event_listener.close()
            self.connect_data_item_reference(data_item_reference)
        self.__data_item_reference_changed_event_listener = (
            data_item_reference.data_item_reference_changed_event.listen(
            data_item_reference_changed))