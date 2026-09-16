def format_json(event, colored):
    try:
        if event.message.startswith('{'):
            msg_dict = json.loads(event.message)
            event.message = json.dumps(msg_dict, indent=2)
    except Exception:
        pass
    return event