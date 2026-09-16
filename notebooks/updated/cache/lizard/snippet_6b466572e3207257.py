def regular_generic_msg(hostname, result, oneline, caption):
    if not oneline:
        return '%s | %s >> %s\n' % (hostname, caption, utils.jsonify(result,
            format=True))
    else:
        return '%s | %s >> %s\n' % (hostname, caption, utils.jsonify(result))