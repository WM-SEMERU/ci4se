def _write_coco_results(self, _coco, detections):
    cats = [cat['name'] for cat in _coco.loadCats(_coco.getCatIds())]
    class_to_coco_ind = dict(zip(cats, _coco.getCatIds()))
    results = []
    for cls_ind, cls in enumerate(self.classes):
        if cls == '__background__':
            continue
        logger.info('collecting %s results (%d/%d)' % (cls, cls_ind, self.
            num_classes - 1))
        coco_cat_id = class_to_coco_ind[cls]
        results.extend(self._coco_results_one_category(detections[cls_ind],
            coco_cat_id))
    logger.info('writing results json to %s' % self._result_file)
    with open(self._result_file, 'w') as f:
        json.dump(results, f, sort_keys=True, indent=4)