def remove_repeated_comments(node):
    last_comment = {'text': None}
    for _node in gast.walk(node):
        if anno.hasanno(_node, 'comment'):
            comment = anno.getanno(_node, 'comment')
            if comment['text'] == last_comment['text']:
                anno.delanno(_node, 'comment')
            last_comment = comment
    return node