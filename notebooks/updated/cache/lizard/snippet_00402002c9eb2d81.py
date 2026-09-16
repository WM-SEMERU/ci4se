def parse_transcript_number(effect):
    name = name_of_associated_transcript(effect)
    if '-' not in name:
        return 0
    parts = name.split('-')
    last_part = parts[-1]
    if last_part.isdigit():
        return int(last_part)
    else:
        return 0