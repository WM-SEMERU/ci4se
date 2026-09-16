def handle_record_clicked(self, callback_fn):
    assert callable(callback_fn)
    if self.__scan_hardware_source:

        def finish_record(data_and_metadata_list):
            record_index = self.__scan_hardware_source.record_index
            for data_and_metadata in data_and_metadata_list:
                data_item = DataItem.DataItem()
                data_item.ensure_data_source()
                display_name = data_and_metadata.metadata.get('hardware_source'
                    , dict()).get('hardware_source_name')
                display_name = display_name if display_name else _('Record')
                channel_name = data_and_metadata.metadata.get('hardware_source'
                    , dict()).get('channel_name')
                title_base = '{} ({})'.format(display_name, channel_name
                    ) if channel_name else display_name
                data_item.title = '{} {}'.format(title_base, record_index)
                data_item.set_xdata(data_and_metadata)
                callback_fn(data_item)
            self.__scan_hardware_source.record_index += 1
        self.__scan_hardware_source.record_async(finish_record)