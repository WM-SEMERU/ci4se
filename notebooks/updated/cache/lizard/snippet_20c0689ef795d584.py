def substitute(ctx, text, old_text, new_text, instance_num=-1):
    text = conversions.to_string(text, ctx)
    old_text = conversions.to_string(old_text, ctx)
    new_text = conversions.to_string(new_text, ctx)
    if instance_num < 0:
        return text.replace(old_text, new_text)
    else:
        splits = text.split(old_text)
        output = splits[0]
        instance = 1
        for split in splits[1:]:
            sep = new_text if instance == instance_num else old_text
            output += sep + split
            instance += 1
        return output