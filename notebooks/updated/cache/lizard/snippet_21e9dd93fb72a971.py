def remove_sort(self, field_name):
    self.sorts = [dict(field=value) for field, value in self.sorts if field
         is not field_name]