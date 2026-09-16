def process_remove_action(processors, action, argument):
    for processor in processors:
        processor(action, argument)
    db.session.commit()