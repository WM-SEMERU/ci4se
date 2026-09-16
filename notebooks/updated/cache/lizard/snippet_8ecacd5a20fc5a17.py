def _update_labels(self, label, pad_box, height, width):
    out = label.copy()
    out[:, (1, 3)] = (out[:, (1, 3)] * width + pad_box[0]) / pad_box[2]
    out[:, (2, 4)] = (out[:, (2, 4)] * height + pad_box[1]) / pad_box[3]
    return out