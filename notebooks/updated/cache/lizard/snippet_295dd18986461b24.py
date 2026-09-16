def get_infobox(ptree, boxterm='box'):
    boxes = []
    for item in lxml.etree.fromstring(ptree).xpath('//template'):
        title = item.find('title').text
        if title and boxterm in title:
            box = template_to_dict(item)
            if box:
                return box
            alt = template_to_dict_alt(item, title)
            if alt:
                boxes.append(alt)
    if boxes:
        return {'boxes': boxes, 'count': len(boxes)}