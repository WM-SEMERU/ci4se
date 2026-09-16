def get_write_fields(self):
    write_fields = self.get_write_subset('record')
    write_fields = write_fields + ['seg_name', 'seg_len']
    if self.comments != None:
        write_fields.append('comments')
    return write_fields