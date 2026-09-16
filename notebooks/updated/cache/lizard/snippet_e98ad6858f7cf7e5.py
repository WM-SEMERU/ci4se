def unicode2str(content):
    if isinstance(content, dict):
        result = {}
        for key in content.keys():
            result[unicode2str(key)] = unicode2str(content[key])
        return result
    elif isinstance(content, list):
        return [unicode2str(element) for element in content]
    elif isinstance(content, int) or isinstance(content, float):
        return content
    else:
        return content.encode('utf-8')