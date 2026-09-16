def strip_html(text):

    def reply_to(text):
        replying_to = []
        split_text = text.split()
        for index, token in enumerate(split_text):
            if token.startswith('@'):
                replying_to.append(token[1:])
            else:
                message = split_text[index:]
                break
        rply_msg = ''
        if len(replying_to) > 0:
            rply_msg = 'Replying to '
            for token in replying_to[:-1]:
                rply_msg += token + ','
            if len(replying_to) > 1:
                rply_msg += 'and '
            rply_msg += replying_to[-1] + '. '
        return rply_msg + ' '.join(message)
    text = reply_to(text)
    text = text.replace('@', ' ')
    return ' '.join([token for token in text.split() if 'http:' not in
        token and 'https:' not in token])