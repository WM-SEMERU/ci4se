def _get_predicton_csv_lines(data, headers, images):
    if images:
        data = copy.deepcopy(data)
        for img_col in images:
            for d, im in zip(data, images[img_col]):
                if im == '':
                    continue
                im = im.copy()
                im.thumbnail((299, 299), Image.ANTIALIAS)
                buf = BytesIO()
                im.save(buf, 'JPEG')
                content = base64.urlsafe_b64encode(buf.getvalue()).decode(
                    'ascii')
                d[img_col] = content
    csv_lines = []
    for d in data:
        buf = six.StringIO()
        writer = csv.DictWriter(buf, fieldnames=headers, lineterminator='')
        writer.writerow(d)
        csv_lines.append(buf.getvalue())
    return csv_lines