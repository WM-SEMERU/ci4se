def map(self, function):
    if isinstance(self.slice, slice):
        for i in range(*self.slice.indices(len(self.layout.fields))):
            function(self.layout.fields[i])
    elif isinstance(self.slice, list):
        for pointer in self.slice:
            position = pointer[0]
            layout_object = self.layout.fields[position[0]]
            for i in position[1:]:
                previous_layout_object = layout_object
                layout_object = layout_object.fields[i]
            if function.__name__ == 'update_attrs' and isinstance(layout_object
                , string_types):
                function(previous_layout_object)
            else:
                function(layout_object)