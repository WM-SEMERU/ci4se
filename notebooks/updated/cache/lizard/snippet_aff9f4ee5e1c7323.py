def _get_img_attrs(self, style, kwargs):
    img_1x, img_2x, size = self._get_renditions(kwargs)
    return {'src': img_1x, 'width': size[0], 'height': size[1], 'srcset': 
        '{} 1x, {} 2x'.format(img_1x, img_2x) if img_1x != img_2x else None,
        'style': ';'.join(style) if style else None, 'class': kwargs.get(
        'class', kwargs.get('img_class')), 'id': kwargs.get('img_id')}