def convert(self, label, units=None, conversion_function=convert_time):
    label_no = self.get_label_no(label)
    new_label, new_column = self.get_converted(label_no, units,
        conversion_function)
    labels = [LabelDimension(l) for l in self.labels]
    labels[label_no] = new_label
    matrix = self.matrix.copy()
    matrix[:, (label_no)] = new_column
    return LabeledMatrix(matrix, labels)