def update_ds_ids_from_file_handlers(self):
    for file_handlers in self.file_handlers.values():
        fh = file_handlers[0]
        res = getattr(fh, 'resolution', None)
        if res is None:
            continue
        for ds_id, ds_info in list(self.ids.items()):
            file_types = ds_info['file_type']
            if not isinstance(file_types, list):
                file_types = [file_types]
            if fh.filetype_info['file_type'] not in file_types:
                continue
            if ds_id.resolution is not None:
                continue
            ds_info['resolution'] = res
            new_id = DatasetID.from_dict(ds_info)
            self.ids[new_id] = ds_info
            del self.ids[ds_id]