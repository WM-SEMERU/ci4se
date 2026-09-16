def inset_sizes(cls, original_width, original_height, target_width,
    target_height):
    if target_width >= original_width and target_height >= original_height:
        target_width = float(original_width)
        target_height = original_height
    elif target_width <= original_width and target_height >= original_height:
        k = original_width / float(target_width)
        target_height = int(original_height / k)
    elif target_width >= original_width and target_height <= original_height:
        k = original_height / float(target_height)
        target_width = int(original_width / k)
    elif target_width < original_width and target_height < original_height:
        k = original_width / float(original_height)
        k_w = original_width / float(target_width)
        k_h = original_height / float(target_height)
        if k_w >= k_h:
            target_height = int(target_width / k)
        else:
            target_width = int(target_height * k)
    return target_width, target_height