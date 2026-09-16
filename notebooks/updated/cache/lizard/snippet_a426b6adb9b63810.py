def overlay_class_names(self, image, predictions):
    scores = predictions.get_field('scores').tolist()
    labels = predictions.get_field('labels').tolist()
    labels = [self.CATEGORIES[i] for i in labels]
    boxes = predictions.bbox
    template = '{}: {:.2f}'
    for box, score, label in zip(boxes, scores, labels):
        x, y = box[:2]
        s = template.format(label, score)
        cv2.putText(image, s, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 
            255, 255), 1)
    return image