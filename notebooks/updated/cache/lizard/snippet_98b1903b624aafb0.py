def _get_display_data_with_images(data, images):
    if not images:
        return data
    display_data = copy.deepcopy(data)
    for img_col in images:
        for d, im in zip(display_data, images[img_col]):
            if im == '':
                d[img_col + '_image'] = ''
            else:
                im = im.copy()
                im.thumbnail((128, 128), Image.ANTIALIAS)
                buf = BytesIO()
                im.save(buf, 'PNG')
                content = base64.b64encode(buf.getvalue()).decode('ascii')
                d[img_col + '_image'] = content
    return display_data