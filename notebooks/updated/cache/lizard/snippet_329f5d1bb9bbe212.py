def __construct_data_item_reference(self, hardware_source: HardwareSource.
    HardwareSource, data_channel: HardwareSource.DataChannel):
    session_id = self.session_id
    key = self.make_data_item_reference_key(hardware_source.
        hardware_source_id, data_channel.channel_id)
    data_item_reference = self.get_data_item_reference(key)
    with data_item_reference.mutex:
        data_item = data_item_reference.data_item
        if data_item is None:
            data_item = DataItem.DataItem()
            data_item.ensure_data_source()
            data_item.title = '%s (%s)' % (hardware_source.display_name,
                data_channel.name
                ) if data_channel.name else hardware_source.display_name
            data_item.category = 'temporary'
            data_item_reference.data_item = data_item

            def append_data_item():
                self.append_data_item(data_item)
                self._update_data_item_reference(key, data_item)
            self.__call_soon(append_data_item)

        def update_session():
            if data_item.session_id != session_id:
                data_item.session_id = session_id
            session_metadata = ApplicationData.get_session_metadata_dict()
            if data_item.session_metadata != session_metadata:
                data_item.session_metadata = session_metadata
            if data_channel.processor:
                src_data_channel = hardware_source.data_channels[
                    data_channel.src_channel_index]
                src_data_item_reference = self.get_data_item_reference(self
                    .make_data_item_reference_key(hardware_source.
                    hardware_source_id, src_data_channel.channel_id))
                data_channel.processor.connect_data_item_reference(
                    src_data_item_reference)
        self.__call_soon(update_session)
        return data_item_reference