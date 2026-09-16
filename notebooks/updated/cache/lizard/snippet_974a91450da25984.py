def get_fields_class(self, class_name):
    l = []
    for i in self.get_classes():
        for j in i.get_fields():
            if class_name == j.get_class_name():
                l.append(j)
    return l