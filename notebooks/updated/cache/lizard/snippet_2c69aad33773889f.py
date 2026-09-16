def visit(spht, node):
    if node.options['target']:
        html_attrs_ah = dict(CLASS='reference external image-reference',
            href=node.options['target'])
        spht.body.append(spht.starttag(node, 'a', '', **html_attrs_ah))
    html_attrs_img = dict(src=node.src, alt=node.options['alt'])
    if node.options['align']:
        html_attrs_img['CLASS'] = 'align-{}'.format(node.options['align'])
    if node.style:
        html_attrs_img['style'] = node.style
    spht.body.append(spht.starttag(node, 'img', '' if node.options['target'
        ] else '\n', **html_attrs_img))