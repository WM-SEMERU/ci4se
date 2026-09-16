def merge(json, firstField, secondField):
    merged = []
    for i in range(0, len(json[firstField])):
        merged.append({json[firstField][i]: json[secondField][i]})
    return merged