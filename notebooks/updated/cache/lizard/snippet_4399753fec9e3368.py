def smallest_url(flickr, pid, min_width, min_height):
    sizes = flickr.photos_getSizes(photo_id=pid, format='parsed-json')
    smallest_url = None
    smallest_area = None
    for size in sizes['sizes']['size']:
        width = int(size['width'])
        height = int(size['height'])
        if width >= min_width and height >= min_height:
            if not smallest_url or height * width < smallest_area:
                smallest_area = height * width
                smallest_url = size['source']
    return smallest_url