def format_location(ctx, text):
    text = conversions.to_string(text, ctx)
    return text.split('>')[-1].strip()