def to_dict(self, img_sets):
    json_obj = super(DefaultPredictionImageSetManager, self).to_dict(img_sets)
    json_obj['images'] = [img_set.to_dict() for img_set in img_sets.images]
    return json_obj