def images(self, fields=None, token=None):
    if 'image' not in self.data:
        return
    out = []
    for img in self.data['image']:
        if token and token not in img['kind']:
            continue
        info = {}
        for key in img:
            if fields and key not in fields:
                continue
            info.update({key: img[key]})
        if info:
            out.append(info)
    return out