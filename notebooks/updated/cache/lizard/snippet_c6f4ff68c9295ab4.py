def regional_atlas(graph, label_image, xxx_todo_changeme1):
    r
    probability_map, alpha = xxx_todo_changeme1
    label_image = scipy.asarray(label_image)
    probability_map = scipy.asarray(probability_map)
    __check_label_image(label_image)
    objects = scipy.ndimage.find_objects(label_image)
    for rid in range(1, len(objects) + 1):
        weight = scipy.sum(probability_map[objects[rid - 1]][label_image[
            objects[rid - 1]] == rid])
        graph.set_tweight(rid - 1, alpha * weight, -1.0 * alpha * weight)