def process_message(message_text):
    message_text = normalize_message(message_text)
    for regex, data_lambda in TEMPLATES:
        match = regex.search(message_text)
        if match:
            result = Request(**data_lambda(match))
            return result