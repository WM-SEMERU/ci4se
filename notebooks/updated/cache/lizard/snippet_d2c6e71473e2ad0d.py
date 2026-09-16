def MarkDown(node):
    cur = node.first_child
    output = []
    while cur is not None:
        t = cur.t
        if t == 'paragraph':
            output.append(paragraph(cur))
        elif t == 'text':
            output.append(text(cur))
        elif t == 'softbreak':
            output.append(softbreak(cur))
        elif t == 'linebreak':
            output.append(hardbreak(cur))
        elif t == 'link':
            output.append(reference(cur))
        elif t == 'heading':
            output.append(title(cur))
        elif t == 'emph':
            output.append(emphasis(cur))
        elif t == 'strong':
            output.append(strong(cur))
        elif t == 'code':
            output.append(literal(cur))
        elif t == 'code_block':
            output.append(literal_block(cur))
        elif t == 'html_inline' or t == 'html_block':
            output.append(raw(cur))
        elif t == 'block_quote':
            output.append(block_quote(cur))
        elif t == 'thematic_break':
            output.append(transition(cur))
        elif t == 'image':
            output.append(image(cur))
        elif t == 'list':
            output.append(listNode(cur))
        elif t == 'item':
            output.append(listItem(cur))
        elif t == 'MDsection':
            output.append(section(cur))
        else:
            print('Received unhandled type: {}. Full print of node:'.format(t))
            cur.pretty()
        cur = cur.nxt
    return output